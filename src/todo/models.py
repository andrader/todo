import uuid
from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class Priority(str, Enum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class TodoBase(BaseModel):
    title: str = Field(..., min_length=1, description="Title of the todo item")
    description: Optional[str] = Field(default=None, description="Detailed description")
    due_date: Optional[datetime] = Field(
        default=None, description="Due date for the task"
    )
    priority: Priority = Field(default=Priority.MEDIUM, description="Task priority")
    category: Optional[str] = Field(default=None, description="Task category")


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    due_date: Optional[datetime] = None
    priority: Optional[Priority] = None
    category: Optional[str] = None


class Todo(TodoBase):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    completed: bool = False
    created_at: datetime = Field(default_factory=datetime.now)

    model_config = ConfigDict(from_attributes=True)
