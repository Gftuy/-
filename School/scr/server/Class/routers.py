from typing import List

from fastapi import APIRouter
from .models import OutputClass, ImputClass, NewId
from .resolvers import add_new_class, get_classs, get_class, update_class

router = APIRouter()


@router.get('/')
def get_class() -> List[OutputClass]:
    return get_classs()


@router.get('/{class_id}')
def get_current_class(class_id: int) -> OutputClass:
    return get_class(class_id)


@router.post('/')
def add_class(new_class: ImputClass) -> NewId:
    return add_new_class(new_class)


@router.put('/{class_id}')
def add_class(class_id: int, new_class: ImputClass) -> NewId:
    return update_class(class_id, new_class)
