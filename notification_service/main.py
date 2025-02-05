from contextlib import asynccontextmanager
from fastapi import FastAPI, Header, Request
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, UTC

from .api.endpoints import router
from .api.schemas import HealthResponse, RootResponse
from .core.config import settings

# Lifespan
@asynccontextmanager
async def lifespan(_: FastAPI):
    print("🚀 Starting Notification Service")
    yield
    print("👋 Shutting down Notification Service")

# FastAPI App
app = FastAPI(
    title=settings.SERVICE_NAME,
    summary=settings.SERVICE_DESCRIPTION,
    version=settings.VERSION,
    lifespan=lifespan,
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Routes
app.include_router(router, prefix="/api/v1")

# Root
@app.get("/", response_model=RootResponse)
async def root(request: Request, user_agent: str | None = Header(default=None)):
    return RootResponse(
        name=settings.SERVICE_NAME,
        description=settings.SERVICE_DESCRIPTION,
        version=settings.VERSION,
        endpoints={
            "root": "/",
            "health": "/health",
            "docs": "/docs",
            "redoc": "/redoc",
            "openapi": "/openapi.json",
            "api_v1": settings.API_PREFIX,
        },
        timestamp=datetime.now(UTC),
        user_agent=user_agent,
        ip_address=request.client.host,
    )

# Health Check
@app.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(
        service=settings.SERVICE_NAME,
        description=settings.SERVICE_DESCRIPTION,
        status="healthy",
        version=settings.VERSION,
        timestamp=datetime.now(UTC),
        environment=settings.ENVIRONMENT,
    )
