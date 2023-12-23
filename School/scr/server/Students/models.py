from pydantic import BaseModel
from typing import Optional, List


class Student(BaseModel):
    id: Optional[int]
    fio: str
    address: str
    class_id: Optional[int]


class StudentGroup(BaseModel):
    class_id: int
    students: List[Student]


class NewId(BaseModel):
    id: str
    code: int
