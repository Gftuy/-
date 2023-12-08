from typing import List

from fastapi import APIRouter
from .models import OutputTime, ImputTime, NewId
from .resolvers import add_new_time, get_time, get_times, delete_current_time

router = APIRouter()


@router.get('/')
def get_time() -> List[OutputTime]:
    return get_times()


@router.get('/{time_id}')
def get_current_time(time_id: int) -> OutputTime:
    return get_time(time_id)


@router.post('/')
def add_time(new_time: ImputTime) -> NewId:
    return add_new_time(new_time)


@router.delete("/{time_id}")
def delete_time(time_id: int) -> NewId:
    return delete_current_time(time_id)