from typing import List
from pydantic import BaseModel


class Class(BaseModel):
    id: int
    number_class: int
    quantity: int
    classroom_teacher: str


class ClassGroup(BaseModel):
    id: int
    number_class: List[Class]
