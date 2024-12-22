from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def read_users():
    return users
@app.post('/user/{username}/{age}')
async def create_user(username: str, age: int):
    # Определяем новый ID на основе максимального ключа
    new_id = str(max(map(int, users.keys()), default=0) + 1)
    user_id = f"Имя: {username}, возраст: {age}"
    users[new_id] = user_id
    return f"User {user_id} is registered"

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description="Введите ID пользователя", example= 1 )],
                      username: Annotated[str, Path(min_length=5, max_length=20,
                                            description="Введите имя пользователя",example="UrbanProfi" )],
                      age: Annotated[int, Path(min_length=18, max_length=76, description="Enter User age",
                                                         example=24)]):
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"Имя: {username}, возраст: {age}"
@app.delete('/user/{user_id}')
async def delete_user(user_id: int, username: str):
    del users[user_id]
    return f"Пользователь с Id номером {user_id} имя {username} удален"
