from fastapi.responses import RedirectResponse
from fastapi import FastAPI
import uvicorn
from db_manager import base_manager
from Students import router as student_router
# from Users import router as user_router
from Class import router as class_router
from Teacher import router as teacher_router
from settings import SCRIPTS_TABLES_PATH, SCRIPTS_RIMARY_DATA_PATH

app = FastAPI()

app.include_router(student_router, prefix='/student')
# app.include_router(user_router, prefix='/users')
app.include_router(class_router, prefix='/class')
app.include_router(teacher_router, prefix='/teacher')


@app.get("/")
def root():
    return RedirectResponse('/docs')


if __name__ == '__main__':
    if not base_manager.check_base():
        base_manager.create_base(SCRIPTS_TABLES_PATH, SCRIPTS_RIMARY_DATA_PATH)
    uvicorn.run(app="start_server:app", host="0.0.0.0", port=8000, reload=True)
