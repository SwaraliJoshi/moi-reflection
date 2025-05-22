from fastapi import FastAPI
from app.handlers import TaskHandler

app = FastAPI()

app.include_router(TaskHandler.router, prefix="/api")
