from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

class person(BaseModel):
    name: str | None = Path(max_length=20,min_length=3,title="This is name")
    age: int | None = Path(title="this is age",ge=0,lt=100)
    id: float | None = Path(gt=0, lt=500)
    email: str | None = "Rohollaramezani@gmail.com"

@app.get("/profile/{name}")
def profile(name:str,age:Optional[int]=Query(gt=0,lt=120)):
    return f"Hello {name} you are {age} years old"


@app.post("/login")
def login(username:str,password:str):
    return {"username":username, "password":password}


@app.post("/registery")
def registery(prs:person):
    return f"You are register {prs}"
