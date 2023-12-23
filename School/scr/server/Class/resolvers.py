from .models import Class, ClassGroup
from db_manager import base_manager


def get_class():
    res = base_manager.execute("SELECT  id, number_class, quantity, classroom_teacher  FROM Class")
    print(res)
    return Class(id=res["id"], number_class=res["number_class"], quantity=res["quantity"],
                 classroom_teacher=res["classroom_teacher"])


def add_class(new_class: ClassGroup):
    res = base_manager.execute("INSERT INTO Class(id, number_class, quantity, classroom_teacher)"
                               " VALUES (?, ?, ?, ?)"
                               "RETURNING id",
                               args=(new_class.id, new_class.number_class, new_class.quantity, new_class.class_teacher))
    return res


def update_class(class_id: int, clas: Class):
    res = base_manager.execute("UPDATE class SET number_class = ?, quantity = ?, classroom_teacher = ? WHERE id = ?",
                               args=(clas.number_class, clas.quantity, clas.classroom_teacher))
    return res


def delete_class(class_id: int):
    res = base_manager.execute("DELETE FROM class WHERE id = ?",
                               args=(class_id,))
    return res
