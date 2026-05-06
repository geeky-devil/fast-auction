from pydantic import BaseModel

class UserBase(BaseModel):
    username:str
    email:str | None 

class UserCreate(BaseModel):
    username:str
    password:str
    email : str = None

class UserResponse(BaseModel):
    id:int
    username:str
    model_config = {
        "from_attributes" : True
    }

class UserUpdate(BaseModel):
    username:str = None
    password:str = None
    email:str = None

class UserLogIn(BaseModel):
    username:str
    password:str