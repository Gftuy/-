from pydantic import BaseModel
from typing import Optional


class ImputTeacher(BaseModel):
    name: str


class OutputTeacher(BaseModel):
    id: int
    name: str


class NewId(BaseModel):
    code: int
    id: int