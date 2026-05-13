from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from app.core.config import settings
from app.internal.jobs import listing_resolver

class ListingScheduler():
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.trigger = IntervalTrigger(seconds = settings.LISTING_RESOLVE_SECONDS)
        self.add_jobs()
    
    def add_jobs(self):
        self.scheduler.add_job(listing_resolver,self.trigger)
    def start(self):
        self.scheduler.start()
    def shutdown(self):
        self.scheduler.shutdown()