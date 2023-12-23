from .models import Student, StudentGroup, NewId
from db_manager import base_manager


def get_student():
    res = base_manager.execute("SELECT id, fio, address, class_id  FROM Student")
    print(res)
    return Student(id=res["id"], fio=res["fio"], address=res["address"], class_id=res["class_id"])


def add_students(new_student: StudentGroup):
    res = base_manager.execute("INSERT INTO Student(id, fio, address, class_id)"
                               " VALUES (?, ?, ?, ?)"
                               "RETURNING id",
                               args=(new_student.class_id, new_student.fio, new_student.address, new_student.class_id))
    return NewId(code=res['code'], id=res['data'][0][0])


def update_student(student_id: int, student: Student):
    res = base_manager.execute("UPDATE students SET fio = ?, address = ? WHERE id = ?",
                               args=(student.fio, student.address))
    return NewId(code=res['code'], id=student_id)


def delete_student(student_id: int):
    res = base_manager.execute("DELETE FROM students WHERE id = ?",
                               args=(student_id,))
    return NewId(code=res['code'], id=student_id)
