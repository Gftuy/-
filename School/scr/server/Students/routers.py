from typing import List

from fastapi import APIRouter
from .models import Student, StudentGroup, NewId
from .resolvers import get_student, add_students, update_student, delete_student

router = APIRouter()


@router.get('/')
def get_student() -> List[StudentGroup]:
    return get_student()


@router.get('/{class_id}')
def get_students_by_group(group_id: int) -> List[Student]:
    return get_student(group_id)


@router.post('/')
def add_student(new_student: Student) -> NewId:
    return add_student(new_student)


@router.put('/{student_id}')
def add_student(student_id: int, new_student: Student) -> NewId:
    return update_student(student_id, new_student)


@router.delete("/{student_id}")
def delete_student(student_id: int) -> NewId:
    return delete_student(student_id)
