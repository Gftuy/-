from typing import List

from fastapi import APIRouter
from .models import OutputObject, ImputObject, NewId
from .resolvers import add_new_object, get_object, get_objects, update_object, delete_current_object

router = APIRouter()


@router.get('/')
def get_object() -> List[OutputObject]:
    return get_objects()


@router.get('/{object_id}')
def get_current_object(object_id: int) -> OutputObject:
    return get_object(object_id)


@router.post('/')
def add_object(new_object: ImputObject) -> NewId:
    return add_new_object(new_object)


@router.put('/{object_id}')
def add_object(object_id: int, new_object: ImputObject) -> NewId:
    return update_object(object_id, new_object)


@router.delete("/{object_id}")
def delete_object(object_id: int) -> NewId:
    return delete_current_object(object_id)