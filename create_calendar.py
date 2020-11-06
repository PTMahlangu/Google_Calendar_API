from config import config
from pprint import pprint
import datetime
import pickle
import os.path


def get_calendar_id():
    service,status = config()
    if status == 201:
        response = service.calendarList().list().execute()
        calendars = response.get('items',[])

        if not calendars:
            return None
            
        for calendar in calendars:
            summary = calendar['summary']
            id = calendar['id']
            if summary =='Code Clinic':
                print(summary,id)
                return id
        return None

            
def create_calendar():
    service,status = config()
    if status == 201 :
        calendar_name ={
            'summary':'Code Clinic'
        }
        response = service.calendars().insert(body=calendar_name).execute()
        return response.get('id')

if __name__ == '__main__':
    print(create_calendar())