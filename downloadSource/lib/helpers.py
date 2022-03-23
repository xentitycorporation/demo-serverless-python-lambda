from datetime import datetime, timedelta

def _getPreviousDayYear(this, days = 1):
    today = datetime.today()
    yesterday = (today - timedelta(days = days))
    return yesterday.year

def _getPreviousDayMonth(this, days = 1):
    today = datetime.today()
    yesterday = (today - timedelta(days = days))
    return yesterday.month

def _getPreviousDayDay(this, days = 1):
    today = datetime.today()
    yesterday = (today - timedelta(days = days))
    return yesterday.day

def _getYear(this):
    return datetime.today().year

def _getMonth(this):
    return datetime.today().month

def _getDay(this):
    return datetime.today().day

helpers = {
    'getYear': _getYear,
    'getMonth': _getMonth,
    'getDay': _getDay,
    'getPreviousDayYear': _getPreviousDayYear,
    'getPreviousDayMonth': _getPreviousDayMonth,
    'getPreviousDayDay': _getPreviousDayDay
}
