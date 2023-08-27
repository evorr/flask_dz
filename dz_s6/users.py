from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request
from forms import *
from database import *
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="templates")
router = APIRouter()


# Создание нового пользователя
@router.post("/users/new/", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(
        name=user.name,
        last_name=user.last_name,
        email=user.email,
        password=user.password)
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}


# Список пользователей
@router.get("/users/", response_model=list[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


# Просмотр одного пользователя
@router.get("/users/id/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


# Редактирование пользователя
@router.put("/users/replace/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update()\
        .where(users.c.id == user_id)\
        .values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}


# Удаление пользователя
@router.delete("/users/del/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}


# Вывод пользователей в HTML
@router.get("/l_us/", response_class=HTMLResponse)
async def list_users(request: Request):
    query = users.select()
    return templates.TemplateResponse("db.html",
                                      {"request": request,
                                       'users': await database.fetch_all(query)})
