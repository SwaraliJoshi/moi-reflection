
from fastapi import APIRouter
from app.models.Task import Task
from app.services import TaskService

router = APIRouter()

@router.get("/ping")
async def ping():
    return {"message": "pong"}

@router.post("/tasks")
async def create(task: Task):
    return {"id": await TaskService.create_task(task)}

@router.get("/tasks")
async def list_tasks():
    return await TaskService.get_all_tasks()

@router.get("/tasks/{task_id}")
async def get_task(task_id: str):
    task = await TaskService.get_task_by_id(task_id)
    return task

@router.put("/tasks/{task_id}")
async def update(task_id: str, task: Task):
    await TaskService.update_task(task_id, task)
    return {"message": "Updated"}

@router.delete("/tasks/{task_id}")
async def delete(task_id: str):
    await TaskService.delete_task(task_id)
    return {"message": "Deleted"}