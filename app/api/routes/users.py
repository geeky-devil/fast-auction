from fastapi import Depends, APIRouter , HTTPException , status
from app.api.deps import SessionDep , CurrentUserDep
import app.services.user_service as Service
from app.schemas.user import *


router = APIRouter(prefix="/users",tags= ['users'])


@router.get("/",response_model = UserResponse)
async def get_user_private(user:CurrentUserDep , db:SessionDep):
    if user is None:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail= "Unauthorized Access")
    return user

'/POST'

@router.post('/',response_model = UserResponse)
def new_user(user:UserCreate, db:SessionDep):
    try:
        return Service.create_user(user,db)
    except HTTPException as e:
        raise e
  

