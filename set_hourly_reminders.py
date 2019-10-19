from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.events', 'https://www.googleapis.com/auth/calendar']
# SCOPES = ['https://www.googleapis.com/auth/calendar']

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # calendar_list_entry = service.calendarList().get(calendarId='r1vbe4l7ra3vrh5kikivt4u704@group.calendar.google.com').execute()
    # print(calendar_list_entry)

    event = {
        'summary': 'Track time',
        'start': {
            'dateTime': '2019-10-19T09:00:00',
            'timeZone': 'America/New_York',
            'colorID': 'Graphite'
        },
        'end': {
            'dateTime': '2019-10-19T09:01:00',
            'timeZone': 'America/New_York'
        }, 
        'recurrence': ['RRULE:FREQ=DAILY;COUNT=10'], 
        'reminders': {
            'useDefault': True,
        },
        }
    for i in range(0, 8):
        print(i)
        event['start']['dateTime'] = '2019-10-19T'+str(i)+':00:00'
        event['end']['dateTime'] = '2019-10-19T'+str(i)+':01:00'
        event_new = service.events().insert(calendarId='r1vbe4l7ra3vrh5kikivt4u704@group.calendar.google.com', body=event).execute()
        print("Event was created")


if __name__ == '__main__':
    main()