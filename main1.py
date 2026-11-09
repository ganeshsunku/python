from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Employee(BaseModel):
    name: str
    email: str
    salary: float

@app.post("/employees")
def create_employee(employee: Employee):
    return {
        "message": "Employee created",
        "employee": employee
    }

@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee: Employee):
    return {"id": employee_id, "employee": employee}

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    return {"message": "Employee deleted"}