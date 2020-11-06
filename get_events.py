from config import config
from pprint import pprint
import datetime
import pickle
import os.path



def get_events(no_of_events):
    service,status = config()
    if status == 201:
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time

        events_result = service.events().list(calendarId='primary', 
                                            timeMin=now,
                                            maxResults=no_of_events, 
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
    get_events(2)