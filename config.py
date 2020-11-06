from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from pprint import pprint


def config():
    """Shows basic usage of the Google Calendar API.
        Returns:
            service                :
    """
    
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

    try:
        service = build(API_SERVICE_NAME, API_VERSION, credentials=creds)
        # print(API_SERVICE_NAME,' service created successfully')
        return service,201
    except Exception as e:
        print(e)
        return None,400

def convert_to_RFC_datetime(year=1900, month=1, day=1, hour=0, minute=0):
    dt = datetime.datetime(year, month, day, hour, minute, 0).isoformat() + 'Z'
    return dt

if __name__ == '__main__':
    service,status =config()
    print(status)