import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class TodoBase(BaseModel):
    title: str = Field(..., min_length=1, description="Title of the todo item")
    description: Optional[str] = Field(default=None, description="Detailed description")


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class Todo(TodoBase):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    completed: bool = False
    created_at: datetime = Field(default_factory=datetime.now)

    model_config = ConfigDict(from_attributes=True)
