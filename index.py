from fastapi import FastAPI,status,HTTPException,Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
app=FastAPI()

templates=Jinja2Templates(directory="template")
class UserIn(BaseModel):
    username:str
    password:str
    email:str
    phone:str


class UserOut(BaseModel):
    username:str
    email:str


@app.post("/",response_model=UserOut,status_code=status.HTTP_206_PARTIAL_CONTENT,response_class=HTMLResponse)
def user(user:UserIn):
    if user.username=="admin":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED ,detail="You can't use Admin as username",headers={"hoooo":"kerm nariz"})
    return user


@app.get("/home",response_class=HTMLResponse)
def home(request: Request,id:int):
    return templates.TemplateResponse(
        request=request, name="index.html",context={"id":id}
    )
