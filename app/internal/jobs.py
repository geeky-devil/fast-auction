from datetime import datetime
from app.core.database import SessionLocal
from app.services.background_service import clean_up_listing

def testfunc():
    print('Scheduled task',datetime.now())

def listing_cleanup():
    db = SessionLocal()
    try:
        clean_up_listing(db)
    except:
        db.rollback()
        raise Exception('Listing clean-up failed,rolling back...')
    finally:
        db.close()
        print('Clean-up Completed! ',datetime.now())