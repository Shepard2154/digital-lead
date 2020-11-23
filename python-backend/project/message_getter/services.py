from datetime import datetime, timedelta
import requests
import json


def get_hour_data(month, day, year, hour, danger='', event=''):
    return _get_graphic_data(month, day, year, r=12, delta=timedelta(minutes=5), event=event, danger=danger, hour=hour)

def get_day_data(month, day, year,  danger='', event=''):
    return _get_graphic_data(month, day, year, r=24, delta=timedelta(hours=1), event=event, danger=danger)

def get_month_data(month, year, danger="", event=""):
    return _get_graphic_data(month, 1, year, delta=timedelta(days=1), event=event, danger=danger)

def get_year_data(year,  danger='', event=''):
    return _get_graphic_data(1, 1, year, r=12, delta=None, event=event, danger=danger)

def _get_graphic_data(month, day, year, delta, hour = 0, danger='', event='', r=40) -> dict:
    response = dict()
    after = datetime(year, month, day, hour, 0, 0)
    for i in range(r):
        if delta:
             before = after + delta
        else:
            if after.month == 12: 
                before = datetime(year=after.year+1, month=1, day=after.day,
                                hour=after.hour, minute=after.minute)
            else: 
                before = datetime(year=after.year, month=after.month+1, day=after.day,
                                hour=after.hour, minute=after.minute)
        r = requests.get(f"http://127.0.0.1:8000/message/get/?date_after={after.isoformat()}Z&date_before={before.isoformat()}&danger={danger}&event={event}")
        cases = json.loads(r.content)
        if delta == timedelta(days=1):
            response[after.day] = len(cases.get('data'))
        if delta == timedelta(hours=1):
            response[after.hour] = len(cases.get('data'))
        if delta == timedelta(minutes=5):
            response[after.minute] = len(cases.get('data'))
        if not delta:
            response[after.month] = len(cases.get('data'))
        after = before
        if r==40: 
            if before.day==1: break
    return response
