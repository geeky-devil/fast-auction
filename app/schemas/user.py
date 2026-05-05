from pydantic import BaseModel

class UserCreate(BaseModel):
    username:str
    email : str = None

class UserResponse(BaseModel):
    username:str
    model_config = {
        "from_attributes" : True
    }

class UserUpdate(BaseModel):
    username:str = None
    password:str = None
    email:str = None
