import io
import logging
import uuid
from typing import Optional, Tuple
from urllib.parse import urlparse

from PIL import Image
from fastapi import UploadFile, BackgroundTasks
from minio import Minio
from minio.error import S3Error

from app.core.config import settings
from app.core.exceptions import BadRequestException

logger = logging.getLogger("culinary_blog.storage")

ALLOWED_MIME_TYPES = {
    "image/jpeg": [b"\xff\xd8\xff"],
    "image/png": [b"\x89PNG\r\n\x1a\n", b"\x89PNG"],
    "image/webp": [b"RIFF"],
    "image/avif": [b"ftypavif", b"ftypavis"],
}

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB (CONS-007)[cite: 5]


class MinIOStorageService:
    def __init__(self):
        self.client: Optional[Minio] = None
        self._connect()

    def _connect(self):
        """Khởi tạo kết nối tới MinIO client."""
        try:
            self.client = Minio(
                endpoint=settings.MINIO_ENDPOINT,
                access_key=settings.MINIO_ACCESS_KEY,
                secret_key=settings.MINIO_SECRET_KEY,
                secure=settings.MINIO_SECURE,
            )
            self._ensure_bucket()
        except Exception as e:
            logger.warning(
                f"Could not connect to MinIO on startup: {e}. Will retry on file operation."
            )
            self.client = None

    def _ensure_bucket(self):
        """Đảm bảo Bucket đã tồn tại và cài đặt policy public read."""
        if not self.client:
            return

        bucket_name = settings.MINIO_BUCKET_NAME
        if not self.client.bucket_exists(bucket_name):
            self.client.make_bucket(bucket_name)
            policy = f"""{{
                "Version": "2012-10-17",
                "Statement": [
                    {{
                        "Effect": "Allow",
                        "Principal": "*",
                        "Action": ["s3:GetObject"],
                        "Resource": ["arn:aws:s3:::{bucket_name}/*"]
                    }}
                ]
            }}"""
            self.client.set_bucket_policy(bucket_name, policy)

    def _get_client(self) -> Optional[Minio]:
        """Thử kết nối lại nếu client chưa sẵn sàng."""
        if self.client is None:
            self._connect()
        return self.client

    async def validate_file(self, file: UploadFile) -> Tuple[bytes, str]:
        """Kiểm tra dung lượng file, định dạng Content-Type và Magic Bytes."""
        content = await file.read()
        await file.seek(0)

        # 1. Kiểm tra kích thước file
        if len(content) > MAX_FILE_SIZE:
            raise BadRequestException(
                error_code="FILE_SIZE_EXCEEDED",
                detail=f"Kích thước file ({len(content) / (1024 * 1024):.2f}MB) vượt quá giới hạn tối đa 5MB.",
            )

        # 2. Kiểm tra MIME Type
        content_type = file.content_type
        if content_type not in ALLOWED_MIME_TYPES:
            raise BadRequestException(
                error_code="FILE_MIME_INVALID",
                detail="Loại file không được phép. Chỉ chấp nhận JPEG, PNG, WebP, AVIF.",
            )

        # 3. Kiểm tra Magic Bytes
        is_magic_valid = False
        magic_signatures = ALLOWED_MIME_TYPES[content_type]
        header_sample = content[:32]

        for sig in magic_signatures:
            if sig in header_sample:
                is_magic_valid = True
                break

        if not is_magic_valid:
            raise BadRequestException(
                error_code="FILE_MIME_INVALID",
                detail="Định dạng file không khớp với nội dung thực tế (magic bytes validation failed).",
            )

        ext = content_type.split("/")[-1]
        if ext == "jpeg":
            ext = "jpg"

        return content, ext

    def process_and_upload_thumbnail(self, content: bytes, original_object_name: str) -> Optional[str]:
        """Background Job: Tạo ảnh thumbnail (300x300 px) và tải lên MinIO (FR-JOB-002)."""
        try:
            image = Image.open(io.BytesIO(content))
            image.thumbnail((300, 300))

            if image.mode in ("RGBA", "P"):
                image = image.convert("RGB")

            thumb_buffer = io.BytesIO()
            image.save(thumb_buffer, format="JPEG", quality=85)
            thumb_bytes = thumb_buffer.getvalue()

            path_parts = original_object_name.split("/")
            folder = path_parts[0] if len(path_parts) > 1 else "recipes"
            file_name = path_parts[-1]
            thumb_object_name = f"{folder}/thumb_{file_name}"

            client = self._get_client()
            bucket_name = settings.MINIO_BUCKET_NAME

            if client:
                client.put_object(
                    bucket_name=bucket_name,
                    object_name=thumb_object_name,
                    data=io.BytesIO(thumb_bytes),
                    length=len(thumb_bytes),
                    content_type="image/jpeg",
                )
                logger.info(f"[BACKGROUND JOB] Đã tạo và lưu ảnh thumbnail thành công: {thumb_object_name}")
                return f"{settings.MINIO_PUBLIC_URL.rstrip('/')}/{bucket_name}/{thumb_object_name}"
        except Exception as e:
            logger.error(f"[BACKGROUND JOB] Lỗi khi tạo thumbnail cho {original_object_name}: {e}", exc_info=True)
        return None

    async def upload_file(
        self,
        file: UploadFile,
        folder: str = "recipes",
        background_tasks: Optional[BackgroundTasks] = None
    ) -> str:
        """Upload file gốc lên MinIO và kích hoạt Background Task tạo thumbnail."""
        content, ext = await self.validate_file(file)
        unique_filename = f"{folder}/{uuid.uuid4()}.{ext}"

        client = self._get_client()
        base_url = settings.MINIO_PUBLIC_URL.rstrip("/")
        bucket_name = settings.MINIO_BUCKET_NAME

        if client:
            try:
                self._ensure_bucket()

                client.put_object(
                    bucket_name=bucket_name,
                    object_name=unique_filename,
                    data=io.BytesIO(content),
                    length=len(content),
                    content_type=file.content_type,
                )

                # Kích hoạt Background Job Resize Ảnh nếu truyền background_tasks
                if background_tasks:
                    background_tasks.add_task(
                        self.process_and_upload_thumbnail,
                        content=content,
                        original_object_name=unique_filename
                    )

                return f"{base_url}/{bucket_name}/{unique_filename}"
            except Exception as e:
                logger.error(f"Failed to upload to MinIO: {e}", exc_info=True)

        return f"{base_url}/{bucket_name}/{unique_filename}"

    async def delete_file(self, file_url: str) -> None:
        """Xóa file trên MinIO dựa theo URL."""
        client = self._get_client()
        if not file_url or not client:
            return

        try:
            bucket_name = settings.MINIO_BUCKET_NAME
            parsed_url = urlparse(file_url)
            path_parts = parsed_url.path.lstrip("/").split("/")

            if len(path_parts) > 1 and path_parts[0] == bucket_name:
                object_name = "/".join(path_parts[1:])
                client.remove_object(bucket_name, object_name)
            else:
                prefix = f"{settings.MINIO_PUBLIC_URL.rstrip('/')}/{bucket_name}/"
                if file_url.startswith(prefix):
                    object_name = file_url[len(prefix) :]
                    client.remove_object(bucket_name, object_name)

        except Exception as e:
            logger.warning(
                f"Error deleting object from MinIO ({file_url}): {e}"
            )


storage_service = MinIOStorageService()