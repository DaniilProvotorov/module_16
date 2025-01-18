from fastapi import FastAPI, Path, HTTPException, Body, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
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

templates = Jinja2Templates(directory='templates')


@app.get('/', response_class=HTMLResponse)
async def all_users(request: Request):
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.get('/user/{user_id}')
async def all_users(request: Request, user_id: int) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'user': users[user_id]})


@app.post('/user/{username}/{age}', response_model=User)
async def add_user(user: User):
    if users:
        user_id = max(users, key=lambda u: u.id).id + 1
    else: user_id = 0
    user = User(id=user_id, username=user.username, age=user.age)
    users.append(user)
    return user


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
