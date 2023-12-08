from .models import OutputClass, ImputClass, NewId
from database.db_manager import base_manager

ID = 0
NAME = 1


def get_classs():
    res = base_manager.execute("SELECT id, name FROM Class", many=True)
    classs = []
    for class in res['data']:
        class.append(OutputClass(id=class[ID], name=class[NAME]))
    return classs


def get_class(class_id: int):
    res = base_manager.execute("SELECT id, name FROM Class WHERE id = ?",
                               args=(class_id,), many=False)
    print(res)
    return OutputClass(id=res["id"], name=res["name"])


def add_new_class(new_class: ImputClass, ):
    res = base_manager.execute("INSERT INTO classs(name) "
                               "VALUES (?) "
                               "RETURNING id", args=(new_class.name,))
    print(res)
    return NewId(code=res['code'], id=res['data'][0][0])


def update_class(class_id: int, class: ImputClass):
    res = base_manager.execute("UPDATE class SET name = ? WHERE id = ?",
                               args=(class.name, class_id,))
    return NewId(code=res['code'], id=class_id)
