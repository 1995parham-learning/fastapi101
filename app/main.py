"""
Main module to run the FastAPI application which is called by uvicorn.
"""

import rich
from fastapi import FastAPI

from app import config
from app.routers import users

settings = config.Settings()
rich.print(f"configuration: {settings.model_dump()}")

app = FastAPI(debug=settings.http.debug)

app.include_router(
    users.router,
    prefix="/users",
)
