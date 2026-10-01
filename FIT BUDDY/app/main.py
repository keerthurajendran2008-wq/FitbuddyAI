from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .config import settings
from .database import init_db
from .routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application startup and shutdown lifecycle.

    The database tables are created automatically when
    the FastAPI application starts.
    """

    init_db()

    yield


app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    description=(
        "FitBuddy is an AI-powered personalized "
        "fitness planning application."
    ),
    lifespan=lifespan,
)


# Serve CSS, JavaScript and other static files.
app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static",
)


# Register application routes.
app.include_router(router)


@app.get("/health")
def health_check():
    """
    Simple endpoint used to verify that the
    FitBuddy backend is running.
    """

    return {
        "status": "ok",
        "service": settings.app_name,
    }