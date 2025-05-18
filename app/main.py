from fastapi import FastAPI
from app.api import task_routes

app = FastAPI()

app.include_router(task_routes.router, prefix="/api")
