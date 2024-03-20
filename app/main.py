"""
Main module to run the FastAPI application which is called by uvicorn.
"""

from fastapi import FastAPI

from app import config
from app.routers import users

app = FastAPI(debug=config.settings.http.debug)

app.include_router(
    users.router,
    prefix="/users",
)
