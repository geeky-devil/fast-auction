from datetime import datetime , timedelta , timezone

def DateTimeNow():
    return datetime.now()
def DateTimeUTCNow():
    return datetime.now(timezone.utc)
