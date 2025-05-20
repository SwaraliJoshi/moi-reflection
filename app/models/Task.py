from datetime import date
from pydantic import BaseModel, Field
from typing import List, Optional

from app.enums.TaskStatus import Status

class Task(BaseModel):
    id: Optional[str] = Field(..., min_length=1)
    title: str
    description: Optional[str] = None
    status: Status = Status.new
    dueDate: date
    tags: Optional[List[str]]