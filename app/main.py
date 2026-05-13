from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.internal.scheduler import ListingScheduler
from app.core.database import init_db
from app.routes import users,admin, auth, items, listings

scheduler = ListingScheduler()

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()    
    scheduler.start()
    yield
    scheduler.shutdown()

app = FastAPI(lifespan=lifespan)

app.include_router(admin.router)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(items.router)
app.include_router(listings.router)