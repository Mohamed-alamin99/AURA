from fastapi import FastAPI

from src.api.routes.health import router as health_router
from src.api.routes.knowledge_bases import router as knowledge_bases_router
from src.core.config import settings


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Enterprise AI Knowledge Platform",
)

app.include_router(health_router)
app.include_router(knowledge_bases_router)