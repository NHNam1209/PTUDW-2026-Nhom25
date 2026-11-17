import asyncio
import logging
import os
from contextlib import asynccontextmanager

try:
    from apscheduler.schedulers.asyncio import AsyncIOScheduler
except ImportError:
    AsyncIOScheduler = None

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.api.v1.auth import router as auth_router
from app.api.v1.categories import router as categories_router
from app.api.v1.dashboard import router as dashboard_router
from app.api.v1.health import router as health_router
from app.api.v1.recipes import router as recipes_router
from app.api.v1.users import router as users_router
from app.core.config import settings
from app.core.database import Base, async_engine
from app.core.logging import setup_logging
from app.core.middleware import (
    correlation_id_middleware,
    rate_limit_middleware,
    register_exception_handlers,
)
from app.jobs.sitemap_job import generate_sitemap_xml

# Configure structured logging with file rotation and audit trail (FR-OBS-002)
logger = setup_logging()

scheduler = AsyncIOScheduler() if AsyncIOScheduler else None


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: create tables if they do not exist
    logger.info("Initializing database tables...")
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Database tables initialized.")

    # FR-JOB-003: Schedule sitemap.xml generation cron job every 24 hours
    if scheduler:
        try:
            scheduler.add_job(
                generate_sitemap_xml,
                "interval",
                hours=24,
                id="sitemap_cron",
                replace_existing=True,
            )
            scheduler.start()
            logger.info("[CRON-JOB] Sitemap scheduler started (interval: 24h).")
        except Exception as e:
            logger.warning(f"Could not start background scheduler: {e}")

    # Initial sitemap generation if not exists
    if not os.path.exists("static/sitemap.xml"):
        asyncio.create_task(generate_sitemap_xml())

    yield

    # Shutdown
    logger.info("Shutting down application...")
    try:
        if scheduler and scheduler.running:
            scheduler.shutdown(wait=False)
    except Exception:
        pass
    await async_engine.dispose()


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Culinary Blog - Hệ thống API Blog Ẩm thực và Nấu ăn theo chuẩn SRS v1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)

# CORS Middleware (NFR-SEC-005)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["X-Correlation-ID", "X-Response-Time"],
)

# Custom Middlewares & Exception Handlers (FR-OBS-002, NFR-SEC-003)
app.middleware("http")(correlation_id_middleware)
app.middleware("http")(rate_limit_middleware)
register_exception_handlers(app)

# Serve static directory if available
os.makedirs("static", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include API Routers under /api/v1
app.include_router(health_router, prefix="")
app.include_router(health_router, prefix=settings.API_V1_STR)
app.include_router(auth_router, prefix=settings.API_V1_STR)
app.include_router(recipes_router, prefix=settings.API_V1_STR)
app.include_router(categories_router, prefix=settings.API_V1_STR)
app.include_router(dashboard_router, prefix=settings.API_V1_STR)
app.include_router(users_router, prefix=settings.API_V1_STR)


@app.get("/sitemap.xml", tags=["SEO"], summary="Dynamic Sitemap XML (FR-JOB-003 / FR-SEO-001)")
async def get_sitemap():
    sitemap_path = os.path.join("static", "sitemap.xml")
    if not os.path.exists(sitemap_path):
        await generate_sitemap_xml()
    return FileResponse(sitemap_path, media_type="application/xml")


@app.get("/", tags=["Root"])
async def root():
    return {
        "name": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "status": "online",
        "docs": "/docs",
        "health": "/health",
        "sitemap": "/sitemap.xml",
    }
