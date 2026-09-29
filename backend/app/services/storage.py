import io
import logging
import uuid
from typing import Optional, Tuple
from urllib.parse import urlparse

from app.core.config import settings
from app.core.exceptions import BadRequestException
from fastapi import UploadFile
from minio import Minio
from minio.error import S3Error

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
            # Public-read policy cho phép đọc ảnh trực tiếp qua URL
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

        # Xác định phần mở rộng đường dẫn (Extension)
        ext = content_type.split("/")[-1]
        if ext == "jpeg":
            ext = "jpg"

        return content, ext

    async def upload_file(self, file: UploadFile, folder: str = "recipes") -> str:
        """Upload file lên MinIO và trả về URL công khai."""
        content, ext = await self.validate_file(file)
        unique_filename = f"{folder}/{uuid.uuid4()}.{ext}"

        client = self._get_client()
        base_url = settings.MINIO_PUBLIC_URL.rstrip("/")
        bucket_name = settings.MINIO_BUCKET_NAME

        if client:
            try:
                # Đảm bảo bucket sẵn sàng trước khi upload
                self._ensure_bucket()

                client.put_object(
                    bucket_name=bucket_name,
                    object_name=unique_filename,
                    data=io.BytesIO(content),
                    length=len(content),
                    content_type=file.content_type,
                )
                return f"{base_url}/{bucket_name}/{unique_filename}"
            except Exception as e:
                logger.error(f"Failed to upload to MinIO: {e}", exc_info=True)

        # Fallback / Development URL khi không kết nối được MinIO
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

            # Kiểm tra xem URL có chứa tên bucket hay không
            if len(path_parts) > 1 and path_parts[0] == bucket_name:
                object_name = "/".join(path_parts[1:])
                client.remove_object(bucket_name, object_name)
            else:
                # Nếu URL không chứa bucket name dạng path
                prefix = f"{settings.MINIO_PUBLIC_URL.rstrip('/')}/{bucket_name}/"
                if file_url.startswith(prefix):
                    object_name = file_url[len(prefix) :]
                    client.remove_object(bucket_name, object_name)

        except Exception as e:
            logger.warning(
                f"Error deleting object from MinIO ({file_url}): {e}"
            )


storage_service = MinIOStorageService()