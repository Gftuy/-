from pydantic import BaseModel
from typing import Optional


class ImputClass(BaseModel):
    name: str


class OutputClass(BaseModel):
    id: int
    name: str


class NewId(BaseModel):
    code: int
    id: int