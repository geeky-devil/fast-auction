from fastapi import FastAPI
from app.core.database import init_db
from app.api.routes import users, admin, auth , items , listings

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(admin.router)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(items.router)
app.include_router(listings.router)