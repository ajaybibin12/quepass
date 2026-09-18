from fastapi import FastAPI

from app.api.router import router as api_router
from app.core.config import settings


def create_application() -> FastAPI:
    """Create and configure the FastAPI application."""
    application = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        debug=settings.debug,
    )

    application.include_router(api_router)

    return application


app = create_application()
