from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel
app = FastAPI()

students = {
    1: {
        "name": "A",
        "age": 12,

    },
    2: {
        "name": "B",
        "age": 12,

    },

}


class Student(BaseModel):
    name: str
    age: int


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None


@app.get("/")
def index():
    return {"name": "Hello"}


@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description="The ID of the student you want to view", gt=0, lt=3)):
    return students[student_id]


@app.get("get-by-name")
def get_student(*, student_id: int, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "not found"}


@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}

    students[student_id] = student
    return students[student_id]


@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Doesn't exists"}
    if students.name != None:
        students[student_id].name = student.name
    if students.age != None:
        students[student_id].age = student.age

    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
        return {"Error": "Doesn't exists"}
    del students[student_id]
    return {"Message": "Student delete"}
