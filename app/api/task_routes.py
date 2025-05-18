
from fastapi import APIRouter
from app.domain.task_model import Task
from app.services import task_service

router = APIRouter()

@router.get("/ping")
async def ping():
    return {"message": "pong"}

@router.post("/tasks")
async def create(task: Task):
    return {"id": await task_service.create_task(task)}

@router.get("/tasks")
async def list_tasks():
    return await task_service.get_all_tasks()

@router.put("/tasks/{task_id}")
async def update(task_id: str, task: Task):
    await task_service.update_task(task_id, task)
    return {"message": "Updated"}

@router.delete("/tasks/{task_id}")
async def delete(task_id: str):
    await task_service.delete_task(task_id)
    return {"message": "Deleted"}