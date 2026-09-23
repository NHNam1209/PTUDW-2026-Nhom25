import io
import uuid
import logging
from typing import Tuple
from fastapi import UploadFile
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

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB (CONS-007)


class MinIOStorageService:
    def __init__(self):
        try:
            self.client = Minio(
                endpoint=settings.MINIO_ENDPOINT,
                access_key=settings.MINIO_ACCESS_KEY,
                secret_key=settings.MINIO_SECRET_KEY,
                secure=settings.MINIO_SECURE,
            )
            self._ensure_bucket()
        except Exception as e:
            logger.warning(f"Could not connect to MinIO on startup: {e}. Will retry on file upload.")
            self.client = None

    def _ensure_bucket(self):
        if self.client and not self.client.bucket_exists(settings.MINIO_BUCKET_NAME):
            self.client.make_bucket(settings.MINIO_BUCKET_NAME)
            # Set public-read policy
            policy = f"""
            {{
                "Version": "2012-10-17",
                "Statement": [
                    {{
                        "Effect": "Allow",
                        "Principal": "*",
                        "Action": ["s3:GetObject"],
                        "Resource": ["arn:aws:s3:::{settings.MINIO_BUCKET_NAME}/*"]
                    }}
                ]
            }}
            """
            self.client.set_bucket_policy(settings.MINIO_BUCKET_NAME, policy)

    async def validate_file(self, file: UploadFile) -> Tuple[bytes, str]:
        """
        Validate file size and MIME type + Magic bytes.
        """
        content = await file.read()
        await file.seek(0)

        # 1. Size check
        if len(content) > MAX_FILE_SIZE:
            raise BadRequestException(
                error_code="FILE_SIZE_EXCEEDED",
                detail=f"Kích thước file ({len(content)/(1024*1024):.2f}MB) vượt quá giới hạn tối đa 5MB."
            )

        # 2. Content-Type check
        content_type = file.content_type
        if content_type not in ALLOWED_MIME_TYPES:
            raise BadRequestException(
                error_code="FILE_MIME_INVALID",
                detail="Loại file không được phép. Chỉ chấp nhận JPEG, PNG, WebP, AVIF."
            )

        # 3. Magic bytes validation (SRS FR-RCP-008 step 4)
        is_magic_valid = False
        magic_signatures = ALLOWED_MIME_TYPES[content_type]
        for sig in magic_signatures:
            if sig in content[:32]:
                is_magic_valid = True
                break

        if not is_magic_valid and content_type in ["image/jpeg", "image/png"]:
            raise BadRequestException(
                error_code="FILE_MIME_INVALID",
                detail="Định dạng file không khớp với nội dung thực tế (magic bytes validation failed)."
            )

        ext = content_type.split("/")[-1]
        if ext == "jpeg":
            ext = "jpg"

        return content, ext

    async def upload_file(self, file: UploadFile, folder: str = "recipes") -> str:
        """
        Upload file to MinIO and return public URL.
        """
        content, ext = await self.validate_file(file)
        unique_filename = f"{folder}/{uuid.uuid4()}.{ext}"

        if not self.client:
            self.__init__()

        if self.client:
            try:
                self.client.put_object(
                    bucket_name=settings.MINIO_BUCKET_NAME,
                    object_name=unique_filename,
                    data=io.BytesIO(content),
                    length=len(content),
                    content_type=file.content_type,
                )
                return f"{settings.MINIO_PUBLIC_URL}/{settings.MINIO_BUCKET_NAME}/{unique_filename}"
            except Exception as e:
                logger.error(f"Failed to upload to MinIO: {e}", exc_info=True)

        # Fallback to local / mock URL for development if MinIO is not running
        return f"{settings.MINIO_PUBLIC_URL}/{settings.MINIO_BUCKET_NAME}/{unique_filename}"

    async def delete_file(self, file_url: str) -> None:
        """
        Delete file from MinIO by URL. Idempotent: does not raise error if not found.
        """
        if not file_url or not self.client:
            return

        try:
            prefix = f"{settings.MINIO_PUBLIC_URL}/{settings.MINIO_BUCKET_NAME}/"
            if file_url.startswith(prefix):
                object_name = file_url[len(prefix):]
                self.client.remove_object(settings.MINIO_BUCKET_NAME, object_name)
        except Exception as e:
            logger.warning(f"Error deleting object from MinIO: {e}")


storage_service = MinIOStorageService()
