from fastapi import APIRouter

from src.core.config import settings

router = APIRouter()


@router.get("/health")
async def health_check():
	return {
		"status": "healthy",
		"service": settings.app_name,
		"environment": settings.environment,
	}
