from typing import List

from fastapi import APIRouter
from .models import OutputTeacher, ImputTeacher, NewId
from .resolvers import add_new_teacher, get_teacher, get_teachers, update_teacher, delete_current_teacher

router = APIRouter()


@router.get('/')
def get_teacher() -> List[OutputTeacher]:
    return get_teachers()


@router.get('/{teacher_id}')
def get_current_teacher(teacher_id: int) -> OutputTeacher:
    return get_teachers(teacher_id)


@router.post('/')
def add_teacher(new_teacher: ImputTeacher) -> NewId:
    return add_new_teacher(new_teacher)


@router.put('/{teacher_id}')
def add_group(teacher_id: int, new_teacher: ImputTeacher) -> NewId:
    return update_teacher(teacher_id, new_teacher)


@router.delete("/{teacher_id}")
def delete_teacher(teacher_id: int) -> NewId:
    return delete_current_teacher(teacher_id)