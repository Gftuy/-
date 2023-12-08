from pydantic import BaseModel
from typing import Optional


class ImputObject(BaseModel):
    name: str


class OutputObject(BaseModel):
    id: int
    name: str


class NewId(BaseModel):
    code: int
    id: int