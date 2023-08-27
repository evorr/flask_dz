import uvicorn as uvicorn
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


users = [
    User(id=1, name='test', email='test@test', password='qwerty'),
    User(id=2, name='ivan', email='ivan@test', password='12345')
]


@app.get("/get/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("list_users.html", {"request": request, "users": users})


@app.post("/user/", response_model=User)
async def user_add(name: str, email: str, password: str):
    id = len(users) + 1
    user = User(id=id, name=name, email=email, password=password)
    users.append(user)
    return user


@app.put("/user/{id}", response_model = User)
async def update_task(id: int, new_name: str, new_email: str, new_passw: str):
    for user in users:
        if user.id == id:
            user.name = new_name
            user.email = new_email
            user.password = new_passw
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/user/{id}")
async def delete_item(id: int):
    for user in users:
        if user.id == id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User not found")

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

