from fastapi import FastAPI, Path

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def all_users():
    return users


@app.post('/user/{username}/{age}')
async def add_user(username: str = Path(max_length=15, min_length=2, discription='Enter username'),
                   age: int = Path(ge=18, le=110, description='Enter age')) -> str:
    user_id = str(int(max(users, key=int))+1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered!'


@app.put('/user/{user_id}/{username_new}/{age_new}')
async def update_data(user_id, username_new: str = Path(max_length=15, min_length=2, discription='Enter new username'),
                      age_new: int = Path(ge=18, le=110, description='Enter new age')) -> str:
    users[user_id] = f'Имя: {username_new}, возраст: {age_new}'
    return f'The user {user_id} is updated!'


@app.delete('/user/user_id')
async def delete_data(user_id) -> str:
    users.pop(user_id)
    return f'The user {user_id} was delete!'
