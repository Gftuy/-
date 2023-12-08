from .models import OutputTime, ImputTime, NewId
from database.db_manager import base_manager

ID = 0
NAME = 1


def get_time():
    res = base_manager.execute("SELECT id, Star_Time, End_Time FROM Time", many=True)
    Time = []
    for Time in res['data']:
        Time.append(OutputTime(id=Time[ID], Start_Time=Time[Start_Time], End_Time=Time[End_Time]))
    return Time


def get_time(time_id: int):
    res = base_manager.execute("SELECT id, Start_Time, End_Time FROM Time WHERE id = ?",
                               args=(time_id,), many=False)
    print(res)
    return OutputTime(id=res["id"], name=res["name"])


def add_new_time(new_time: ImputTime):
    res = base_manager.execute("INSERT INTO Time(Start_Time, End_Time) "
                               "VALUES (?) "
                               "RETURNING id", args=(new_time.Start_Time, End_Time,))
    print(res)
    return NewId(code=res['code'], id=res['data'][0][0])


def update_time(time_id: int, Time: ImputTime):
    res = base_manager.execute("UPDATE times SET name = ? WHERE id = ?",
                               args=(time.Start_Time, time_id, End_Time))
    return NewId(code=res['code'], id=time_id)
