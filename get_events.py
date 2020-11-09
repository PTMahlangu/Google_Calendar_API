from config import config
from pprint import pprint
import datetime
import pickle
import os.path


def get_events(no_days=1):
    service,status = config()
    if status == 201:
        today = datetime.datetime.today()
        max_days = (today + datetime.timedelta(days = no_days)).isoformat() + 'Z' 
        events_result = service.events().list(calendarId='primary', 
                                            timeMin=today.isoformat() + 'Z',
                                            timeMax = max_days,
                                            maxResults=no_days, 
                                            singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
        for i,event in enumerate(events):
            start = event['start'].get('dateTime', event['start'].get('date'))
            end = event['end'].get('dateTime', event['start'].get('date'))
            print(f'{i+1}.', event['summary'],'-',start[:10],'-',start[11:16],'to',end[11:16])

            

if __name__ == '__main__':
    get_events()
