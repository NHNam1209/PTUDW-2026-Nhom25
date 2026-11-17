import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.mark.asyncio
async def test_correlation_id_middleware():
    """FR-OBS-002: Ensure every response contains X-Correlation-ID and X-Response-Time."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        # Request with client-supplied correlation ID
        custom_id = "test-corr-id-12345"
        res = await client.get("/", headers={"X-Correlation-ID": custom_id})
        assert res.status_code == 200
        assert res.headers.get("X-Correlation-ID") == custom_id
        assert "X-Response-Time" in res.headers

        # Request without correlation ID -> Server automatically generates UUID
        res_auto = await client.get("/")
        assert res_auto.status_code == 200
        assert "X-Correlation-ID" in res_auto.headers
        assert len(res_auto.headers["X-Correlation-ID"]) > 10
