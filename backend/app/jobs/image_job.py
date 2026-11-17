import io
import logging
from typing import Optional
from PIL import Image

from app.services.storage import storage_service

logger = logging.getLogger("culinary_blog.jobs.image")


async def generate_and_upload_thumbnail(file_bytes: bytes, original_filename: str) -> Optional[str]:
    """FR-JOB-002: Background job to resize an uploaded image into a 300x300 thumbnail
    and persist it to MinIO S3 Object Storage.
    """
    try:
        image = Image.open(io.BytesIO(file_bytes))
        image.thumbnail((300, 300), Image.Resampling.LANCZOS)

        buffer = io.BytesIO()
        img_format = image.format or "JPEG"
        if img_format.upper() == "PNG":
            image.save(buffer, format="PNG", optimize=True)
            content_type = "image/png"
            ext = "png"
        elif img_format.upper() == "WEBP":
            image.save(buffer, format="WEBP", quality=85)
            content_type = "image/webp"
            ext = "webp"
        else:
            if image.mode in ("RGBA", "P"):
                image = image.convert("RGB")
            image.save(buffer, format="JPEG", quality=85, optimize=True)
            content_type = "image/jpeg"
            ext = "jpg"

        buffer.seek(0)
        base_name = original_filename.rsplit(".", 1)[0]
        thumb_filename = f"thumb_{base_name}.{ext}"

        thumb_url = await storage_service.upload_bytes(
            data=buffer.getvalue(),
            filename=thumb_filename,
            content_type=content_type,
            folder="thumbnails",
        )
        logger.info(f"[JOB-IMAGE] Successfully generated thumbnail: {thumb_url}")
        return thumb_url
    except Exception as e:
        logger.error(
            f"[JOB-IMAGE] Failed to generate thumbnail for {original_filename}: {e}",
            exc_info=True,
        )
        return None
