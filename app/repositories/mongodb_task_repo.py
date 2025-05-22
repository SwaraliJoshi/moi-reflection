from fastapi import HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from app.core.config import settings
from app.models.Task import Task

class MongoDBTaskRepository:
    def __init__(self):
        self.client = AsyncIOMotorClient(settings.MONGO_DB_URL)
        self.db = self.client[settings.DB_NAME]
        self.collection = self.db["tasks"]

    async def create(self, task: Task):
        if task.dueDate is None:
            raise HTTPException(status_code=400, detail="dueDate must be provided")
        result = await self.collection.insert_one(task.dict(exclude={"id"}))
        return str(result.inserted_id)

    async def get_all(self):
        tasks = await self.collection.find().to_list(1000)
        for task in tasks:
            task["id"] = str(task["_id"])
            del task["_id"]
        return tasks
    
    async def get(self, task_id: str):
        try:
            task = await self.collection.find_one({"_id": ObjectId(task_id)})
            task["id"] = str(task["_id"])
            del task["_id"]
            return task
        except:
            return None

    async def update(self, task_id: str, updatedTask: Task):
        try:
            task = await self.collection.find_one({"_id": ObjectId(task_id)})
            task["description"] = updatedTask.description
            task["status"] = updatedTask.status
            task["tags"] = updatedTask.tags
            await self.collection.update_one({"_id": ObjectId(task_id)}, {"$set": {k: v for k, v in task.items() if k != "id"}})
        except Exception as e:
            print(f"Error updating task: {e}")
            return None

    async def delete(self, task_id: str):
        await self.collection.delete_one({"_id": ObjectId(task_id)})
