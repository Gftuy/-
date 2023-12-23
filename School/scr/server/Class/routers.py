from typing import List

from fastapi import APIRouter
from .models import Class, ClassGroup
from .resolvers import get_class, add_class, update_class, delete_class

router = APIRouter()


@router.get('/')
def get_class() -> List[ClassGroup]:
    return get_class()


@router.get('/{class_id}')
def get_class_(class_id: int) -> List[Class]:
    return get_class(class_id)


@router.post('/')
def add_class(new_class: Class):
    return add_class(new_class)


@router.put('/{class_id}')
def add_class(class_id: int, new_class: Class):
    return update_class(class_id, new_class)
