from app.domain.task_model import Task
from app.infrastructure.mongodb_task_repo import MongoDBTaskRepository

repo = MongoDBTaskRepository()

async def create_task(task: Task):
    return await repo.create(task)

async def get_all_tasks():
    return await repo.get_all()

async def update_task(task_id: str, task: Task):
    return await repo.update(task_id, task)

async def delete_task(task_id: str):
    return await repo.delete(task_id)
