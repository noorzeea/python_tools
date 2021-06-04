from datetime import date, time, timedelta

def deltaDays(day):
    """
    Checks if input day is in 7 days
    """
    today = date.today()
    delta = day - today

    return delta.days

def isCurrentWeek(day):
    """
    Checks if input day is in 7 days
    """
    return deltaDays(day) <= 7

def naturalDatetime(input_datetime):
    """
    Translate system's datetime format into a human readable one
    """
    today = date.today()
    time = input_datetime.strftime('%H:%M')
    natural_datetime = date(input_datetime.year, input_datetime.month, input_datetime.day)

    if natural_datetime == today:
        return 'Today' + ' @' + time
    elif natural_datetime == today + timedelta(days=1):
        return 'Tomorrow' + ' @' + time
    elif isCurrentWeek(natural_datetime):
        return 'In' + deltaDays(natural_datetime) + ' days'

    return input_datetime.strftime('%d/%m/%Y') + " @" + input_datetime.strftime('%H:%M')