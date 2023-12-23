from typing import List

from fastapi import APIRouter
from .models import Teacher, TeacherGroup, NewId
from .resolvers import get_teacher, add_teachers, update_teacher, delete_teacher

router = APIRouter()


@router.get('/')
def get_teacher() -> List[TeacherGroup]:
    return get_teacher()


@router.get('/{teacher_id}')
def get_teacher_by_group(teacher_id: int) -> List[Teacher]:
    return get_teacher(teacher_id)


@router.post('/')
def add_teacher(new_teacher: Teacher) -> NewId:
    return add_teacher(new_teacher)


@router.put('/{teacher_id}')
def add_teacher(teacher_id: int, new_teacher: Teacher) -> NewId:
    return update_teacher(teacher_id, new_teacher)


@router.delete("/{teacher_id}")
def delete_teacher(teacher_id: int) -> NewId:
    return delete_teacher(teacher_id)
