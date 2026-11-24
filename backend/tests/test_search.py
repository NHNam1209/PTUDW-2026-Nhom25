import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app
from app.core.database import async_engine


@pytest.mark.asyncio
async def test_search_recipes_full_text():
    """FR-SRCH-001: Full-Text Search with ranking and unaccent support."""
    await async_engine.dispose()
    try:
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as client:
            # 1. Search with Vietnamese accented query
            res = await client.get("/api/v1/recipes/search?q=phở")
            assert res.status_code == 200
            data = res.json()
            assert "items" in data
            assert "meta" in data
            assert data["meta"]["total"] >= 1
            # Top result should contain "Phở" in title
            top_title = data["items"][0]["title"].lower()
            assert "phở" in top_title or "pho" in top_title

            # 2. Search with unaccented query "bo"
            res_bo = await client.get("/api/v1/recipes/search?q=bo")
            assert res_bo.status_code == 200
            data_bo = res_bo.json()
            assert data_bo["meta"]["total"] >= 1

            # 3. Test list recipes with q query param
            res_list = await client.get("/api/v1/recipes?q=gà")
            assert res_list.status_code == 200
            data_list = res_list.json()
            assert data_list["meta"]["total"] >= 1
    finally:
        await async_engine.dispose()

