from pydantic import BaseModel
from typing import Optional


class ImputTime(BaseModel):
    name: str


class OutputTime(BaseModel):
    id: int
    name: str


class NewId(BaseModel):
    code: int
    id: int