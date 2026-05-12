from fastapi import  APIRouter , HTTPException , status
from typing import List
from app.api.deps import SessionDep , CurrentUserDep
from app.schemas.listing import *
import app.services.listing_service as Service

router = APIRouter(prefix="/listing",tags=["listing"])

#---/public routes/---#
@router.get('/all',response_model=List[ListingGet])
def get_all_active_listings(db:SessionDep):
    return Service.get_all(db)


#---/protected routes/---#
@router.get('/',response_model= List[ListingGet])
def get_listings_private(user:CurrentUserDep,db:SessionDep):
    return Service.get_all_private(user,db)

@router.post('/',response_model=ListingGet)
def create_listing(new_listing:ListingCreate,user:CurrentUserDep,db:SessionDep):
    return Service.create_listing(new_listing,user,db)

@router.post('/remove')
def remove_all_listings(user:CurrentUserDep,db:SessionDep):
    return Service.remove_all(user,db)
