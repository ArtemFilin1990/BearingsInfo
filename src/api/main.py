"""
Основной файл FastAPI приложения.

Точка входа для запуска API сервера.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
import logging
import os

from app import APP_DESCRIPTION, APP_NAME, APP_VERSION
from app.api import router as api_router, autocomplete_engine, search_engine

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Создание приложения FastAPI
app = FastAPI(
    title=APP_NAME,
    description=APP_DESCRIPTION,
    version=APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
)

# The API is same-origin by default. Cross-origin clients require an explicit allowlist.
# Never combine wildcard origins with credentialed browser requests.
allowed_origins = [origin.strip() for origin in os.getenv("BEARINGS_CORS_ORIGINS", "").split(",") if origin.strip()]
if "*" in allowed_origins:
    raise RuntimeError("BEARINGS_CORS_ORIGINS must contain concrete origins, not *")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=bool(allowed_origins),
    allow_methods=["GET", "POST", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)

@app.get("/")
async def root():
    """Корневой endpoint"""
    return {
        "message": "Bearing API",
        "version": APP_VERSION,
        "status": "ready",
        "docs": "/docs"
    }

@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "healthy"}

@app.get("/ready")
async def readiness():
    """Readiness requires actual search and autocomplete data, unlike liveness."""
    catalogue_index = bool(search_engine.documents)
    autocomplete_index = bool(autocomplete_engine.terms)
    ready = catalogue_index and autocomplete_index
    return JSONResponse(
        status_code=200 if ready else 503,
        content={
            "status": "ready" if ready else "not_ready",
            "catalogue_index": catalogue_index,
            "autocomplete_index": autocomplete_index,
            "auto_replace_allowed": False,
        },
    )


app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=False,
        log_level="info"
    )
