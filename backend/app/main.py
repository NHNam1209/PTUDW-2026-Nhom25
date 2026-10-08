import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from app.core.config import settings
from app.core.database import async_engine, Base
from app.core.middleware import correlation_id_middleware, register_exception_handlers
from app.api.v1.auth import router as auth_router
from app.api.v1.recipes import router as recipes_router
from app.api.v1.categories import router as categories_router
from app.api.v1.health import router as health_router
from app.jobs.sitemap_job import generate_sitemap_xml

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] (%(name)s) %(message)s",
)
logger = logging.getLogger("culinary_blog")

# Khởi tạo Cron Job Scheduler
scheduler = AsyncIOScheduler()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Khởi tạo database tables
    logger.info("Initializing database tables...")
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Database tables initialized.")

    # Tích hợp Cron Job (FR-JOB-003): Chạy lúc 00:00 hàng ngày
    scheduler.add_job(generate_sitemap_xml, CronTrigger(hour=0, minute=0))
    scheduler.start()
    logger.info("Cron Job Scheduler đã được kích hoạt.")

    # Khởi tạo sitemap ban đầu khi ứng dụng start
    await generate_sitemap_xml()

    yield

    # Shutdown
    logger.info("Shutting down application...")
    scheduler.shutdown()
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

# Phục vụ file sitemap.xml công khai
app.mount("/static", StaticFiles(directory="static"), name="static")

# CORS Middleware (NFR-SEC-005)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["X-Correlation-ID", "X-Response-Time"],
)

# Custom Middlewares & Exception Handlers
app.middleware("http")(correlation_id_middleware)
register_exception_handlers(app)

# Include API Routers
app.include_router(health_router, prefix="")
app.include_router(health_router, prefix=settings.API_V1_STR)
app.include_router(auth_router, prefix=settings.API_V1_STR)
app.include_router(recipes_router, prefix=settings.API_V1_STR)
app.include_router(categories_router, prefix=settings.API_V1_STR)


@app.get("/", tags=["Root"])
async def root():
    return {
        "name": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "status": "online",
        "docs": "/docs",
        "health": "/health",
        "sitemap": "/static/sitemap.xml",
    }