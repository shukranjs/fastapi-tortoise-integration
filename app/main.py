import logging

from fastapi import FastAPI
from app.api.v1.endpoint import router
from tortoise import Tortoise
from contextlib import asynccontextmanager
from config import init_db

log = logging.getLogger()


app = FastAPI(docs_url="/docs")


@app.on_event("startup")
async def startup_event():
    await init_db()


app.include_router(router, prefix="/models", tags=["Models"])
