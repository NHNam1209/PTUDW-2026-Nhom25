from datetime import datetime, timezone
import logging
import os
import xml.etree.ElementTree as ET

from sqlalchemy import select

from app.core.database import async_session_maker
from app.domain.enums import RecipeStatus
from app.domain.models.category import Category
from app.domain.models.recipe import Recipe

logger = logging.getLogger("culinary_blog.jobs.sitemap")


async def generate_sitemap_xml() -> str:
    """FR-JOB-003: Cron job that dynamically generates static/sitemap.xml for SEO indexing."""
    logger.info("[CRON-JOB] Generating sitemap.xml...")
    recipes = []
    categories = []

    try:
        async with async_session_maker() as db:
            # 1. Fetch published recipes
            recipe_stmt = select(Recipe.slug, Recipe.updated_at).where(
                Recipe.status == RecipeStatus.Published.value,
                Recipe.is_deleted == False,
            )
            recipe_res = await db.execute(recipe_stmt)
            recipes = recipe_res.all()

            # 2. Fetch categories
            cat_stmt = select(Category.slug).where(Category.is_deleted == False)
            cat_res = await db.execute(cat_stmt)
            categories = cat_res.scalars().all()
    except Exception as e:
        logger.warning(f"[CRON-JOB] Could not fetch DB records for sitemap ({e}). Proceeding with static URLs.")

    base_url = "https://culinaryblog.com"
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

    def append_url(loc: str, changefreq: str = "weekly", priority: str = "0.8", lastmod: str = None):
        entry = ET.SubElement(urlset, "url")
        ET.SubElement(entry, "loc").text = loc
        if lastmod:
            ET.SubElement(entry, "lastmod").text = lastmod
        ET.SubElement(entry, "changefreq").text = changefreq
        ET.SubElement(entry, "priority").text = priority

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Static Pages
    append_url(f"{base_url}/", changefreq="daily", priority="1.0", lastmod=today)
    append_url(f"{base_url}/recipes", changefreq="daily", priority="0.9", lastmod=today)
    append_url(f"{base_url}/categories", changefreq="weekly", priority="0.8", lastmod=today)

    # Categories
    for cat_slug in categories:
        append_url(f"{base_url}/categories/{cat_slug}", changefreq="weekly", priority="0.8", lastmod=today)

    # Recipes
    for item in recipes:
        slug = item[0]
        updated_at = item[1]
        mod_date = updated_at.strftime("%Y-%m-%d") if updated_at else today
        append_url(f"{base_url}/recipes/{slug}", changefreq="weekly", priority="0.9", lastmod=mod_date)

    os.makedirs("static", exist_ok=True)
    sitemap_path = os.path.join("static", "sitemap.xml")

    tree = ET.ElementTree(urlset)
    ET.indent(tree, space="  ", level=0)
    tree.write(sitemap_path, encoding="utf-8", xml_declaration=True)

    logger.info(
        f"[CRON-JOB] Successfully created sitemap.xml at {sitemap_path} "
        f"({len(recipes)} recipes, {len(categories)} categories)."
    )
    return sitemap_path
