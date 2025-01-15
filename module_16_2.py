from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get('/')
async def starter() -> str:
    return 'Главная страница'


@app.get('/user/admin')
async def admin() -> str:
    return 'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def id_connect(user_id: int = Path(ge=1, le=100, description='Enter user id')) -> str:
    return f'Вы вошли как {user_id}'


@app.get('/user/{username}/{age}')
async def address_bar(username: str = Path(max_length=5, min_length=20, description='Enter username'),
                      age: int = Path(ge=18, le=120, description='Enter age')) -> str:
    return f'Вывошли как {username} и вам {age} лет'
