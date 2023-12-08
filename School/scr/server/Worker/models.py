from pydantic import BaseModel
from typing import Optional


class Worker(BaseModel):
    id: Optional[int]
    name: str
    Post: str


class WorkerGroup(BaseModel):
    Post_id: int
    workers: List[worker]


class NewId(BaseModel):
    code: int
    id: int