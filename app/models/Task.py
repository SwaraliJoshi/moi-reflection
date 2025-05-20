from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Optional

from app.enums.TaskStatus import Status

class Task(BaseModel):
    id: Optional[str] = None
    title: str
    description: Optional[str] = None
    status: Status = Status.new
    dueDate: datetime 
    tags: Optional[List[str]]