from fastapi import FastAPI, Path, HTTPException, Body
from pydantic import BaseModel
from typing import List


class User(BaseModel):
    id: int
    username: str
    age: int


class UserUpdate(BaseModel):
    username: str
    age: int


app = FastAPI()

users: List[User] = []


@app.get('/users', response_model=List[User])
async def all_users():
    return users


@app.post('/user/{username}/{age}', response_model=User)
async def add_user(user: User):
    new_id = max((u.id for u in users), default=0) +1
    new_user = User(id=new_id, username=user.username, age=user.age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{new_username}/{new_age}', response_model=User)
async def update_user(user_id: int, user_update: UserUpdate):
    for i in users:
        if i.id == user_id:
            i.username = user_update.username
            i.age = user_update.age
            return i
    raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id: int):
    for k, u in enumerate(users):
        if u.id == user_id:
            del users[k]
            return users
    raise HTTPException(status_code=404, detail='User was not found')





