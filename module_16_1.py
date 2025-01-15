from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def starter() ->str:
    return 'Главная страница'


@app.get('/user/admin')
async def admin() ->str:
    return 'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def id_connect(user_id: str) ->str:
    return f'Вы вошли как {user_id}'


@app.get('/user')
async def address_bar(name: str, age: str) -> str:
    return f'Вывошли как {name} и вам {age} лет'
