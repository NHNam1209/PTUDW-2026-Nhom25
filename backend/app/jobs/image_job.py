from PIL import Image
import io
from app.services.storage import storage_service

async def generate_and_upload_thumbnail(file_bytes: bytes, original_filename: str):
    """Nhận bytes của ảnh, thu nhỏ về kích thước 300x300 và upload lên MinIO"""
    # Mở ảnh bằng Pillow
    image = Image.open(io.BytesIO(file_bytes))
    image.thumbnail((300, 300)) # Thu nhỏ giữ nguyên tỷ lệ
    
    # Lưu ảnh đã resize vào bộ nhớ tạm
    buffer = io.BytesIO()
    img_format = image.format if image.format else 'JPEG'
    image.save(buffer, format=img_format)
    buffer.seek(0)
    
    # Upload ảnh thumbnail lên thư mục thumbnails trên MinIO
    thumb_name = f"thumbnails/thumb_{original_filename}"
    return await storage_service.upload_file(buffer.getvalue(), thumb_name, f"image/{img_format.lower()}")