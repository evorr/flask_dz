import uvicorn as uvicorn
from fastapi import FastAPI
import users
import items
import orders
import database

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.database.disconnect()


app.include_router(users.router, tags=['users'])
app.include_router(items.router, tags=['items'])
app.include_router(orders.router, tags=['orders'])

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
