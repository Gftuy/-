from pydantic import BaseModel
from typing import Optional, List


class Teacher(BaseModel):
    id: Optional[int]
    fio: str
    address: str
    post: str
    classroom_teacher: Optional[int]


class TeacherGroup(BaseModel):
    id: int
    teacher: List[Teacher]


class NewId(BaseModel):
    id: str
    code: int
