from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request
from forms import *
from database import *
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="templates")
router = APIRouter()


# Добавить товар
@router.post("/items/new/", response_model=Item)
async def create_item(item: AddItem):
    query = items.insert().values(
        name=item.name,
        description=item.description,
        price=item.price)
    last_record_id = await database.execute(query)
    return {**item.dict(), "id": last_record_id}


# Список всех товаров
@router.get("/items/", response_model=list[Item])
async def read_items():
    query = items.select()
    return await database.fetch_all(query)


# Просмотр одного товара
@router.get("/items/id/{item_id}", response_model=Item)
async def read_item(item_id: int):
    query = items.select().where(items.c.id == item_id)
    return await database.fetch_one(query)


# Редактирование товара
@router.put("/items/replace/{item_id}", response_model=User)
async def update_item(item_id: int, new_item: AddItem):
    query = items.update()\
        .where(items.c.id == item_id)\
        .values(**new_item.dict())
    await database.execute(query)
    return {**new_item.dict(), "id": item_id}


# Удаление товара
@router.delete("/items/del/{item_id}")
async def delete_item(item_id: int):
    query = items.delete().where(items.c.id == item_id)
    await database.execute(query)
    return {'message': 'Item deleted'}


# Вывод товаров в HTML
@router.get("/print_items/", response_class=HTMLResponse)
async def list_items(request: Request):
    query = items.select()
    return templates.TemplateResponse("print_items.html",
                                      {"request": request,
                                       'items': await database.fetch_all(query)})