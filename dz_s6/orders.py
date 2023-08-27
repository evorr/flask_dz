from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request
from forms import *
from database import *
from fastapi.responses import HTMLResponse


templates = Jinja2Templates(directory="templates")
router = APIRouter()


# Добавить товар
@router.post("/orders/new/", response_model=Order)
async def create_order(order: AddOrder):
    query = orders.insert().values(
        user_id=order.user_id,
        item_id=order.item_id,
        created_on=order.created_on,
        status=True)
    last_record_id = await database.execute(query)
    return {**order.dict(), "id": last_record_id}


# Список всех заказов
@router.get("/orders/", response_model=list[Order])
async def read_orders():
    query = orders.select()
    return await database.fetch_all(query)


# Просмотр одного заказа
@router.get("/oders/id/{order_id}", response_model=Order)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_one(query)


# Редактирование заказа
@router.put("/orders/replace/{order_id}", response_model=Order)
async def update_order(order_id: int, new_order: AddOrder):
    query = orders.update()\
        .where(orders.c.id == order_id)\
        .values(**new_order.dict())
    await database.execute(query)
    return {**new_order.dict(), "id": order_id}


# Удаление заказа
@router.delete("/orders/del/{order_id}")
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {'message': 'Order deleted'}


# Вывод заказов в HTML
@router.get("/print_orders/", response_class=HTMLResponse)
async def list_orders(request: Request):
    query = orders.select()
    return templates.TemplateResponse("print_orders.html",
                                      {"request": request,
                                       'orders': await database.fetch_all(query)})