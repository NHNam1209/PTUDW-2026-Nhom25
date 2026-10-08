import logging
import os
from datetime import datetime
from sqlalchemy import select
from app.core.database import AsyncSessionLocal
from app.domain.models.recipe import Recipe, RecipeStatus
from app.domain.models.category import Category

logger = logging.getLogger("culinary_blog.cron")


async def generate_sitemap_xml() -> None:
    """Cron Job: Tự động quét cơ sở dữ liệu và khởi tạo file static/sitemap.xml."""
    logger.info("[CRON JOB] Bắt đầu quá trình tạo file sitemap.xml...")
    try:
        async with async_session_maker() as db:
            # 1. Lấy tất cả công thức đã xuất bản
            recipe_stmt = select(Recipe.slug, Recipe.updated_at).where(
                Recipe.status == RecipeStatus.Published.value,
                Recipe.is_deleted == False
            )
            recipe_res = await db.execute(recipe_stmt)
            recipes = recipe_res.all()

            # 2. Lấy tất cả danh mục chưa bị xóa
            cat_stmt = select(Category.slug).where(Category.is_deleted == False)
            cat_res = await db.execute(cat_stmt)
            categories = cat_res.scalars().all()

        # 3. Xây dựng nội dung XML
        domain = "https://culinaryblog.com"
        xml_lines = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        ]

        # Trang chủ
        xml_lines.append(f'  <url>\n    <loc>{domain}/</loc>\n    <changefreq>daily</changefreq>\n    <priority>1.0</priority>\n  </url>')

        # Các danh mục
        for cat_slug in categories:
            xml_lines.append(f'  <url>\n    <loc>{domain}/categories/{cat_slug}</loc>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>')

        # Các bài viết công thức
        for slug, updated_at in recipes:
            lastmod = updated_at.strftime("%Y-%m-%d") if updated_at else datetime.now().strftime("%Y-%m-%d")
            xml_lines.append(f'  <url>\n    <loc>{domain}/recipes/{slug}</loc>\n    <lastmod>{lastmod}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.9</priority>\n  </url>')

        xml_lines.append('</urlset>')

        # 4. Ghi file ra thư mục static
        os.makedirs("static", exist_ok=True)
        sitemap_path = os.path.join("static", "sitemap.xml")
        with open(sitemap_path, "w", encoding="utf-8") as f:
            f.write("\n".join(xml_lines))

        logger.info(f"[CRON JOB] Xuất file sitemap.xml thành công tại đường dẫn: {sitemap_path}")

    except Exception as e:
        logger.error(f"[CRON JOB] Xảy ra lỗi trong quá trình tạo sitemap.xml: {e}", exc_info=True)