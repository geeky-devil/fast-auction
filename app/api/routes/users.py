from fastapi import Depends, APIRouter , HTTPException , status
from app.api.deps import SessionDep
import app.services.user_service as Service
from app.schemas.user import *


router = APIRouter(prefix="/users",tags= ['users'])


@router.get("/{user_id}",response_model = UserResponse)
def get_user(user_id:int, db:SessionDep):
    user = Service.get_user(user_id,db)
    if user is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "User not found")
    return user

@router.post('/',response_model = UserResponse)
def new_user(user:UserCreate, db:SessionDep):
    try:
        n_user = Service.create_user(user,db)
        return n_user
    except HTTPException as e:
        raise e

#     # TODO : create config for dummys?
