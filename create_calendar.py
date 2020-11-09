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
            
        for calendar in calendars:
            summary = calendar['summary']
            id = calendar['id']
            if summary =='Code Clinic':
                return id

        id = create_calendar()
        return id

            
def create_calendar():
    
    service,status = config()
    if status == 201 :
        calendar_name ={
            'summary':'Code Clinic'
        }
        response = service.calendars().insert(body=calendar_name).execute()
        return response.get('id')

if __name__ == '__main__':
    id = get_calendar_id()
    print(id)
