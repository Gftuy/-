from .models import Teacher, TeacherGroup, NewId
from db_manager import base_manager


def get_teacher():
    res = base_manager.execute("SELECT id, fio, address, post, classroom_teacher  FROM Teacher")
    print(res)
    return Teacher(id=res["id"], fio=res["fio"], address=res["address"], post=res["post"],
                   classroom_teacher=res["classroom_teacher"])


def add_teachers(new_teacher: TeacherGroup):
    res = base_manager.execute("INSERT INTO Teacher(id, fio, address, post, classroom_teacher)"
                               " VALUES (?, ?, ?, ?, ?)"
                               "RETURNING id", args=(
    new_teacher.teacher_id, new_teacher.fio, new_teacher.address, new_teacher.post, new_teacher.classroom_teacher))
    return NewId(code=res['code'], id=res['data'][0][0])


def update_teacher(teacher_id: int, teacher: Teacher):
    res = base_manager.execute("UPDATE Teacher SET fio = ?, address = ?, post = ? WHERE id = ?",
                               args=(teacher.fio, teacher.address, teacher.post))
    return NewId(code=res['code'], id=teacher_id)


def delete_teacher(teacher_id: int):
    res = base_manager.execute("DELETE FROM teachers WHERE id = ?",
                               args=(teacher_id,))
    return NewId(code=res['code'], id=teacher_id)
