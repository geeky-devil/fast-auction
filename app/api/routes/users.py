from fastapi import Depends, APIRouter , HTTPException , status
from app.api.deps import SessionDep , CurrentUserDep
import app.services.user_service as Service
from app.schemas.user import *


router = APIRouter(prefix="/users",tags= ['users'])


@router.get("/",response_model = UserResponse)
async def get_user_private(user:CurrentUserDep , db:SessionDep):
    return user

'/POST'

@router.post('/',response_model = UserResponse)
async def new_user(user:UserCreate, db:SessionDep):
    return Service.create_user(user,db)

  

