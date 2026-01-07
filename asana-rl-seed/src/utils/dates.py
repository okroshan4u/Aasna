import random
from datetime import datetime, timedelta

def random_date(start, end):
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))

def avoid_weekends(date):
    if date.weekday() >= 5:
        return date + timedelta(days=(7 - date.weekday()))
    return date
