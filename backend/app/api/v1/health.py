from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.core.database import get_db
from app.core.config import settings
import redis.asyncio as aioredis
from app.services.storage import storage_service

router = APIRouter(tags=["Health Checks"])


@router.get("/health/live", status_code=status.HTTP_200_OK, summary="Liveness probe (FR-OBS-001)")
async def liveness():
    """
    Checks if the process is alive. Always returns 200 unless process has crashed.
    """
    return {"status": "Healthy", "probe": "liveness"}


@router.get("/health/ready", summary="Readiness probe (FR-OBS-001)")
async def readiness(response: Response, db: AsyncSession = Depends(get_db)):
    """
    Checks if database and Redis are reachable.
    Fails (503) if database is unreachable.
    """
    checks = {}
    is_healthy = True

    # 1. Database check
    try:
        await db.execute(text("SELECT 1"))
        checks["database"] = {"status": "Healthy"}
    except Exception as e:
        checks["database"] = {"status": "Unhealthy", "error": str(e)}
        is_healthy = False

    # 2. Redis check
    try:
        r = aioredis.from_url(settings.REDIS_URL, socket_timeout=2.0)
        await r.ping()
        await r.close()
        checks["redis"] = {"status": "Healthy"}
    except Exception as e:
        checks["redis"] = {"status": "Unhealthy", "error": str(e)}
        # In development, Redis might not be fatal, but per SRS FR-OBS-001: readiness checks DB and Redis
        is_healthy = False

    if not is_healthy:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE

    return {
        "status": "Healthy" if is_healthy else "Unhealthy",
        "probe": "readiness",
        "entries": checks,
    }


@router.get("/health", summary="Aggregated Health Check (FR-OBS-001)")
async def health(response: Response, db: AsyncSession = Depends(get_db)):
    """
    Comprehensive health check for DB, Redis, and MinIO.
    """
    entries = {}
    is_healthy = True

    # DB
    try:
        await db.execute(text("SELECT 1"))
        entries["database"] = {"status": "Healthy"}
    except Exception as e:
        entries["database"] = {"status": "Unhealthy", "error": str(e)}
        is_healthy = False

    # Redis
    try:
        r = aioredis.from_url(settings.REDIS_URL, socket_timeout=2.0)
        await r.ping()
        await r.close()
        entries["redis"] = {"status": "Healthy"}
    except Exception as e:
        entries["redis"] = {"status": "Degraded", "error": str(e)}

    # MinIO
    try:
        if storage_service.client:
            storage_service.client.bucket_exists(settings.MINIO_BUCKET_NAME)
            entries["minio"] = {"status": "Healthy"}
        else:
            entries["minio"] = {"status": "Degraded", "error": "Client not initialized"}
    except Exception as e:
        entries["minio"] = {"status": "Degraded", "error": str(e)}

    if not is_healthy:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE

    return {
        "status": "Healthy" if is_healthy else "Unhealthy",
        "entries": entries,
    }
