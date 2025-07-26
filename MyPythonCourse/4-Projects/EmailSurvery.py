from __future__ import print_function
import os.path
import base64
import pandas as pd
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
CREDENTIALS_FILE = 'credentials.json'
TOKEN_FILE = 'token.json'

def authenticate_gmail():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
    service = build('gmail', 'v1', credentials=creds)
    return service

def search_emails(service, query):

def get_email_details(service, msg_id):


def main():
    service = authenticate_gmail()
    keywords = ['thank you for', 'Deine Bewerbung']  # Replace with your keywords
    email_data = []

    for keyword in keywords:
        messages = search_emails(service, keyword)
        for msg in messages:
            subject, message, date = get_email_details(service, msg['id'])
            email_data.append({'Date': date, 'Email Title': subject, 'Message Content': message})

    # Create a DataFrame
    df = pd.DataFrame(email_data)

    # Save to Excel
    df.to_excel('emails.xlsx', index=False, engine='openpyxl')

if __name__ == '__main__':
    main()
