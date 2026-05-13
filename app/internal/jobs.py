from datetime import datetime
from app.core.database import SessionLocal
from app.services.background_service import resolve_listing

def testfunc():
    print('Scheduled task',datetime.now())

def listing_resolver():
    db = SessionLocal()
    try:
        resolve_listing(db)
    except:
        db.rollback()
        raise Exception('Listing resolution failed, rolling back...')
    finally:
        db.close()
        print('Listings resolved! ',datetime.now())