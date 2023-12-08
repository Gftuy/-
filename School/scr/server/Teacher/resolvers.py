from .models import OutputTeacher, ImputTeacher, NewId
from database.db_manager import base_manager

ID = 0
NAME = 1


def get_teachers():
    res = base_manager.execute("SELECT id, name FROM Teacher", many=True)
    teachers = []
    for teacher in res['data']:
        teachers.append(OutputTeacher(id=teacher[ID], name=teacher[NAME]))
    return teachers


def get_teacher(teacher_id: int):
    res = base_manager.execute("SELECT id, name FROM teacher WHERE id = ?",
                               args=(teacher_id,), many=False)
    print(res)
    return OutputTeacher(id=res["id"], name=res["name"])


def add_new_group(new_teacher: ImputTeacher, ):
    res = base_manager.execute("INSERT INTO teachers(name) "
                               "VALUES (?) "
                               "RETURNING id", args=(new_teacher.name,))
    print(res)
    return NewId(code=res['code'], id=res['data'][0][0])


def update_teacher(teacher_id: int, teacher: ImputTeacher):
    res = base_manager.execute("UPDATE teachers SET name = ? WHERE id = ?",
                               args=(teacher.name, teacher_id,))
    return NewId(code=res['code'], id=teacher_id)


def delete_current_teacher(teacher_id: int):
    res = base_manager.execute("DELETE FROM teachers WHERE id = ?",
                               args=(teacher_id,))
    return NewId(code=res['code'], id=teacher_id)