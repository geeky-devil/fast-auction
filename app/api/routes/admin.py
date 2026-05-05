from fastapi import APIRouter
from app.api.deps import SessionDep
import app.models as Models
router = APIRouter(prefix='/admin',tags = ['admin'])

@router.post('/purge_user')
def remove_users(db:SessionDep):
    users = db.query(Models.User).delete()
    db.commit()
    return { 'All users removed'}