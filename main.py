from fastapi import FastAPI, Path
from typing import Annotated
from pydantic import BaseModel

# Создаем экземпляр приложения FastAPI
app = FastAPI()

message_bd = {"0": "First post in Fastapp"}
@app.get("/")
async def root_get_all_messages()-> dict:
    return message_bd

@app.get("/message/{message_id}")
async def root_get_message_by(message_id: str) -> dict:
    return message_bd[message_id]

@app.post("/message")
async def create_message(message: str) -> str:
    current_index = str(int(max(message_bd,key=int))+1)
    message_bd[current_index] = message
    return "Message created"

@app.put("/message/{message_id}")
async def update_message(message_id: str, message:str) -> str:
    message_bd[message_id] = message
    return "Message updated"

@app.delete("/message/{message_id}")
async def delete_message(message_id: str) -> str:
    message_bd.pop(message_id)
    return f"Message deleted {message_id} was deleted"

@app.delete("/")
async def delete_all_messages() -> str:
    message_bd.clear()
    return "All messages deleted"