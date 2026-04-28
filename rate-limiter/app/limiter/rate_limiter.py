from datetime import datetime, timedelta
from app.core.config import Limit, Window

request_log = {}

def check_limit(user_id):
    now = datetime.now()

    if user_id not in request_log:
        request_log[user_id] = []

    # remove old requests
    request_log[user_id] = [
        t for t in request_log[user_id]
        if now - t < timedelta(seconds=Window)
    ]

    remaining = Limit - len(request_log[user_id])

    if remaining <= 0:
        return False, 0

    request_log[user_id].append(now)
    return True, remaining - 1