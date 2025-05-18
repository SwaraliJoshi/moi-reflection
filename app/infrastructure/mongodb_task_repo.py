from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from app.core.config import settings
from app.domain.task_model import Task

class MongoDBTaskRepository:
    def __init__(self):
        self.client = AsyncIOMotorClient(settings.MONGO_URL)
        self.db = self.client[settings.DB_NAME]
        self.collection = self.db["tasks"]

    async def create(self, task: Task):
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

    async def update(self, task_id: str, task: Task):
        await self.collection.update_one({"_id": ObjectId(task_id)}, {"$set": task.dict(exclude={"id"})})

    async def delete(self, task_id: str):
        await self.collection.delete_one({"_id": ObjectId(task_id)})
