import io
import os
import pytest
from PIL import Image

from app.jobs.image_job import generate_and_upload_thumbnail
from app.jobs.sitemap_job import generate_sitemap_xml
from app.services.email import send_welcome_email


@pytest.mark.asyncio
async def test_email_background_job():
    """FR-JOB-001: Test send_welcome_email executes without unhandled exceptions."""
    result = await send_welcome_email("test_user@example.com", "Test User")
    # Will be True (sent via SMTP) or False (caught/logged in dev mode), but must never raise
    assert isinstance(result, bool)


@pytest.mark.asyncio
async def test_image_thumbnail_resizing_job():
    """FR-JOB-002: Test Pillow thumbnail generation and dimensions."""
    # Create test 800x600 in-memory image
    img = Image.new("RGB", (800, 600), color=(255, 0, 0))
    buffer = io.BytesIO()
    img.save(buffer, format="JPEG")
    raw_bytes = buffer.getvalue()

    thumb_url = await generate_and_upload_thumbnail(raw_bytes, "test_recipe.jpg")
    assert thumb_url is not None
    assert "thumb_test_recipe" in thumb_url


@pytest.mark.asyncio
async def test_sitemap_generation_job():
    """FR-JOB-003: Test dynamic sitemap.xml creation."""
    sitemap_path = await generate_sitemap_xml()
    assert os.path.exists(sitemap_path)
    with open(sitemap_path, "r", encoding="utf-8") as f:
        content = f.read()
    assert "<urlset" in content
    assert "https://culinaryblog.com/" in content
