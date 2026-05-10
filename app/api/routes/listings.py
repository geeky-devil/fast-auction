from fastapi import  APIRouter , HTTPException , status
from typing import List
from app.api.deps import SessionDep , CurrentUserDep
from app.schemas.listing import *
import app.services.listing_service as Service

router = APIRouter(prefix="/listing",tags=["listing"])

#---/public routes/---#
@router.get('/',response_model=List[ListingGet])
def get_all_active_listings(db:SessionDep):
    return Service.get_all(db)


#---/protected routes/---#
@router.post('/',response_model=ListingGet)
def create_listing(new_listing:ListingCreate,user:CurrentUserDep,db:SessionDep):
    return Service.create_listing(new_listing,user,db)
