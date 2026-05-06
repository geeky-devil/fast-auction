import app.services.auth_service as AuthService
from fastapi import APIRouter , HTTPException , status
from app.core.security import create_access_token
from app.schemas.auth import Token
from app.api.deps import SessionDep , FormData


router = APIRouter(prefix='/auth',tags= ['auth'])

@router.post('/token',response_model = Token)
async def login_for_access_token(form_data:FormData,db:SessionDep):
    user = AuthService.authenticate_user(form_data.username,form_data.password,db)
    if not user:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,detail = "Invalid Credentials")
    
    access_token = create_access_token(user.username,user.id)
    return Token(access_token = access_token , token_type= 'bearer')