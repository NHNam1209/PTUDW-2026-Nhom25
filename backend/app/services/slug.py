import re
from unidecode import unidecode
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


def generate_slug(text: str) -> str:
    """
    Generate SEO-friendly slug from text.
    Transliterates Vietnamese accents and replaces special characters with hyphens.
    Example: 'Phở Bò Nam Định!' -> 'pho-bo-nam-dinh'
    """
    text = unidecode(text).lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    text = text.strip("-")
    return text or "slug"


async def get_unique_slug(db: AsyncSession, model, title: str, current_id=None) -> str:
    """
    Ensures slug uniqueness in table. If slug exists, appends -2, -3, etc.
    """
    base_slug = generate_slug(title)
    slug = base_slug
    counter = 1

    while True:
        stmt = select(model).where(model.slug == slug)
        if current_id:
            stmt = stmt.where(model.id != current_id)
        result = await db.execute(stmt)
        existing = result.scalar_one_or_none()

        if not existing:
            return slug

        counter += 1
        slug = f"{base_slug}-{counter}"
