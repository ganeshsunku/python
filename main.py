# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import Optional

# app=FastAPI()

# class Details(BaseModel):
#     id:int
#     name:str
#     mail_id:Optional[str]=None
#     location: str


# @app.get("/employee_details")
# def details(
#     employee_details:Details
# ):
#     return employee_details


# @app.delete("/employee_details/{employee_id}")
# def delete_employee_details(employee_id:int):
#     return {"message":"Deleted successfully"}
from fastapi import FastAPI

from main3 import router

app = FastAPI()

app.include_router(router)