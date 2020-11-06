from config import config,convert_to_RFC_datetime
import pickle
import os.path
from pprint import pprint

def create_event(title,description,calendar_id,time_from=[2020, 11, 6, 16, 30],time_to=[2020, 11, 6, 17, 30]):
    service,status = config()
    if status == 201:
        event = {
        'summary': title,
        'description': description,
        'start': {
            'dateTime': convert_to_RFC_datetime(time_from[0],time_from[1], time_from[2], time_from[3], time_from[4]),
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': convert_to_RFC_datetime(time_to[0],time_to[1], time_to[2], time_to[3], time_to[4]),
            'timeZone': 'America/Los_Angeles',
        },
        'attendees': [
            {'email': 'pimahlan@wethinkcode.co.za'},
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
            calendarId=calendar_id, 
            body=event
            ).execute()
        print("Event created successfully")
            

if __name__ == '__main__':
    create_event(title,description,calendar_id,time_from=[2020, 11, 6, 16, 30],time_to=[2020, 11, 6, 17, 30])