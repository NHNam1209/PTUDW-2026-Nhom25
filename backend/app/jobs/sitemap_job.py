import xml.etree.ElementTree as ET
import os

async def generate_sitemap_xml():
    """Tự động tạo file sitemap.xml lưu vào thư mục static"""
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    
    # Danh sách URL cần SEO
    static_urls = ["/", "/recipes", "/categories", "/about"]
    for url_path in static_urls:
        url = ET.SubElement(urlset, "url")
        ET.SubElement(url, "loc").text = f"https://culinaryblog.com{url_path}"
        
    # Tạo thư mục static nếu chưa có
    os.makedirs("static", exist_ok=True)
    
    tree = ET.ElementTree(urlset)
    tree.write("static/sitemap.xml", encoding="utf-8", xml_declaration=True)
    print("[CRON-JOB] Đã tạo thành công file static/sitemap.xml")