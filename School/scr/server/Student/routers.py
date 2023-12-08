from typing import List

from fastapi import APIRouter
from .models import Student, StudentGroup
from .resolvers import get_students

router = APIRouter()


@router.get('/{group_id}')
def get_students_by_group(group_id: int) -> List[Student]:
    return get_students(group_id)
