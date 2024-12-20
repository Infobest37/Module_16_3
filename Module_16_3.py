from fastapi import FastAPI, Path

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
async def update_user(user_id: int, username: str, age: int):
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"
@app.delete('/user/{user_id}')
async def delete_user(user_id: int):
    del users[user_id]
    return f"The user {user_id} is deleted"
