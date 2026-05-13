from fastapi import  APIRouter , HTTPException , status
from typing import List
from app.core.deps import SessionDep , CurrentUserDep
from app.schemas.item import ItemGet , ItemCreate
import app.services.item_service as Service

#TODO : add router dependency
router = APIRouter(prefix="/items",tags=['items'])

@router.get('/{item_id}')
async def get_item(item_id:int,user:CurrentUserDep,db:SessionDep):
    return Service.get_item(user.id,item_id,db)
    
@router.get('/',response_model= List[ItemGet])
async def get_all(user:CurrentUserDep,db:SessionDep):
    return Service.get_all_items(user,db)

"@Post"

@router.post('/',response_model=ItemGet)
async def add_item(item:ItemCreate,user:CurrentUserDep,db:SessionDep):
    return Service.add_item(user.id,item,db)