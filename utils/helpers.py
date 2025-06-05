from datetime import datetime, timedelta

def get_date_plus_days(days=3):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    return future_date.strftime("%d.%m.%Y")