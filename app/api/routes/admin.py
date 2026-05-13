from fastapi import APIRouter
from app.core.deps import SessionDep
from app.core.models import User
router = APIRouter(prefix='/admin',tags = ['admin'])

@router.post('/purge_user')
def remove_users(db:SessionDep):
    users = db.query(User).delete()
    db.commit()
    return { 'All users removed'}