from config import config
import pickle
import os.path
from pprint import pprint
import datetime


def create_event(title,distription):
    service,status = config()
    if status == 201:
        event = {
        'summary': title,
        'description': distription,
        'start': {
            'dateTime': datetime.datetime(year=2020, month=11, day=10, hour=8, minute=0).isoformat() + 'Z',
            'timeZone': 'Africa/Johannesburg',
        },
        'end': {
            'dateTime': datetime.datetime(year=2020, month=11, day=10, hour=9, minute=0).isoformat() + 'Z',
            'timeZone': 'Africa/Johannesburg',
        },
        'attendees': [
            # {'email': 'pimahlan@student.wethinkcode.co.za'},
            {'email': 'mahlangupt.1010@gmail.com'},

        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
            {'method': 'email', 'minutes': 24 * 60},
            {'method': 'popup', 'minutes': 10},
            ],
        },
        }

        event = service.events().insert(
            calendarId='primary', 
            body=event
            ).execute()
        print("Event created successfully")
            

if __name__ == '__main__':
    
    create_event("WETHINKCODE","group projet")
