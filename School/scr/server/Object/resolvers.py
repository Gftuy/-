from .models import OutputObject, ImputObject, NewId
from database.db_manager import base_manager

ID = 0
NAME = 1


def get_objects():
    res = base_manager.execute("SELECT id, name FROM Object", many=True)
    objects = []
    for object in res['data']:
        objects.append(OutputObject(id=object[ID], name=objects[NAME]))
    return objects


def get_object(object_id: int):
    res = base_manager.execute("SELECT id, name FROM Object WHERE id = ?",
                               args=(object_id,), many=False)
    print(res)
    return OutputObject(id=res["id"], name=res["name"])


def add_new_object(new_object: ImputObject, ):
    res = base_manager.execute("INSERT INTO object(name) "
                               "VALUES (?) "
                               "RETURNING id", args=(new_object.name,))
    print(res)
    return NewId(code=res['code'], id=res['data'][0][0])


def update_object(object_id: int, object: ImputObject):
    res = base_manager.execute("UPDATE objects SET name = ? WHERE id = ?",
                               args=(object.name,object_id,))
    return NewId(code=res['code'], id=object_id)


def delete_current_object(object_id: int):
    res = base_manager.execute("DELETE FROM objects WHERE id = ?",
                               args=(object_id,))
    return NewId(code=res['code'], id=object_id)