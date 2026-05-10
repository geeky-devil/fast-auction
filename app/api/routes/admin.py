from fastapi import APIRouter
from app.api.deps import SessionDep
from app.models import User
router = APIRouter(prefix='/admin',tags = ['admin'])

@router.post('/purge_user')
def remove_users(db:SessionDep):
    users = db.query(User).delete()
    db.commit()
    return { 'All users removed'}