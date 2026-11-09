from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import asyncio

class User(BaseModel):
    id:int
    name:str
    email_id: Optional[str]=None
    location:str

app=FastAPI()

@app.get("/user_details")
async def get_user(user:User):
    return user