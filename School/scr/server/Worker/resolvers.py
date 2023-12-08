from .models import Worker, WorkerGroup, NewId
from database.db_manager import base_manager

ID = 0
NAME = 1


def get_worker(group_id: int):
    res = base_manager.execute("SELECT S.id, S.FIO, S.Post "
                               "FROM Worker S "
                               "INNER JOIN group_workers GS ON GS.worker_id = S.id "
                               "WHERE GS.Post_id = ?", args=(Post_id, ), many=True)
    workers = []
    print(res)
    for worker in res['data']:
        workers.append(Worker(id=worker[ID], surname=worker[FIO], name=worker[Post]))
    return worker


def add_new_worker(new_worker: Worker, ):
    res = base_manager.execute("INSERT INTO Worker(FIO, Post) "
                               "VALUES (?, ?) "
                               "RETURNING id", args=(new_worker.FIO, new_worker.Post,))
    return NewId(code=res['code'], id=res['data'][0][0])


def update_worker(worker_id: int, worker: Worker):
    res = base_manager.execute("UPDATE workers SET FIO = ?, Post = ?",
                               args=(worker.FIO, worker.Post))
    return NewId(code=res['code'], id=id)


def delete_worker(worker_id: int):
    res = base_manager.execute("DELETE FROM workers WHERE id = ?",
                               args=(worker_id,))
    return NewId(code=res['code'], id=worker_id)