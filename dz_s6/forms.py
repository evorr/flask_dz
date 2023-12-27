from pydantic import BaseModel, Field
from datetime import datetime


class UserIn(BaseModel):
    name: str = Field(max_length=32)
    last_name: str = Field(max_length=32)
    email: str = Field(max_length=128)
    password: str = Field(max_length=32)


class User(UserIn):
    id: int


class AddItem(BaseModel):
    name: str = Field(max_length=32)
    description: str = Field(max_length=128)
    price: float = Field(ge=0)


class Item(AddItem):
    id: int


class AddOrder(BaseModel):
    user_id: int = Field(...)
    item_id: int = Field(...)
    created_on: datetime
    status: bool


class Order(AddOrder):
    id: int