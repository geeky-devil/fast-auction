import app.models
from fastapi import FastAPI
from app.core.database import init_db
from app.api.routes import users , admin

app = FastAPI()


@app.on_event("startup")
def on_startup():
    init_db()
    print('DB initialized')

app.include_router(admin.router)
app.include_router(users.router)
