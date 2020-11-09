from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from pprint import pprint


class code_clinic():

    def __init__(self):
        self.calendar_id ='' 
        CLIENT_SECRET_FILE = '.credentials.json'
        API_SERVICE_NAME   = 'calendar'
        API_VERSION        = 'v3'
        SCOPES             = ['https://www.googleapis.com/auth/calendar']

        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('.token.pickle'):
            with open('.token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    CLIENT_SECRET_FILE, SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('.token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build(API_SERVICE_NAME, API_VERSION, credentials=creds)


    def create_event(self,title,distription):
        """ This method creates an event in google calender
            argument:
            title       : str (event title)
            distription : str (event distription)
            return:  none
        """
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

        event = self.service.events().insert(
            # calendarId= 'primary',  # remember 
            calendarId= self.get_calendar_id('primary'), 
            body=event
            ).execute()
        print("Event created successfully")


    def get_events(self,no_days=1):
        """ This method print a list of event 
            argument:
            no_days = int (number of days events to be return)
            return:  none
        """
        today = datetime.datetime.today()
        max_days = (today + datetime.timedelta(days = no_days)).isoformat() + 'Z' 
        events_result = self.service.events().list(calendarId='primary', 
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


    def get_calendar_id(self,calendar_name):
        """ This method check if calendar is created, if not it create a calendar and returns calandar id
            argument: none
            return:  calendar id
        """
        response = self.service.calendarList().list().execute()
        calendars = response.get('items',[])
            
        for calendar in calendars:
            summary = calendar['summary']
            self.calendar_id = calendar['id']
            if summary == calendar_name:
                return self.calendar_id

        self.calendar_id = self.create_calendar(calendar_name)
        return self.calendar_id

                
    def create_calendar(self,calendar_name):
        """ This method creates  calender and return it calandar id
            argument: none
            return:  calandar id
        """
        calendar_name ={
            'summary':calendar_name
        }
        response = self.service.calendars().insert(body=calendar_name).execute()
        self.calendar_id = response.get('id')
        return self.calendar_id 


if __name__ == '__main__':

    my = code_clinic()
    my.get_events(3)
    # title = input("Title: ")
    # distription = input("Distription: ")
    # my.create_event(title,distription)
    