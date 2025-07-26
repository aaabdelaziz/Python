import os
import pickle
import base64
import re
import pandas as pd
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email.utils import parsedate_to_datetime

# If modifying these scopes, delete token.json
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
    results = service.users().messages().list(userId='me', q=query).execute()
    messages = results.get('messages', [])
    return messages

def get_email_details(service, msg_id):
    msg = service.users().messages().get(userId='me', id=msg_id, format='full').execute()

    headers = msg['payload'].get('headers', [])
    subject = ''
    date_str = ''
    for header in headers:
        if header['name'] == 'Subject':
            subject = header['value']
        if header['name'] == 'Date':
            date_str = header['value']

    # Parse the date to format dd.mm.yy
    try:
        dt = parsedate_to_datetime(date_str)
        date_formatted = dt.strftime('%d.%m.%y')
    except:
        date_formatted = ''

    # Get message body
    message_body = ''
    if 'parts' in msg['payload']:
        for part in msg['payload']['parts']:
            if 'body' in part and 'data' in part['body']:
                message_body = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
                break
    if not message_body and 'body' in msg['payload'] and 'data' in msg['payload']['body']:
        message_body = base64.urlsafe_b64decode(msg['payload']['body']['data']).decode('utf-8')

    return subject, message_body, date_formatted

def main():
    service = authenticate_gmail()
    keywords = ['thank you for', 'Bewerbung', 'Ihre Bewerbung', 'GmbH']  # Adjust keywords as needed
    email_data = []

    for keyword in keywords:
        print(f"Searching for keyword: {keyword}")
        messages = search_emails(service, keyword)
        for msg in messages:
            subject, message, date = get_email_details(service, msg['id'])
            email_data.append({'Date': date, 'Email Title': subject, 'Message Content': message})

    # Create DataFrame
    df = pd.DataFrame(email_data)

    # Sort by date in ascending order
    # Even if some dates are blank, handle gracefully
    df = df[df['Date'].astype(bool)]  # Remove empty date entries if any
    # No need to convert to datetime as already formatted
    # But for safety, sort assuming 'Date' in 'dd.mm.yy' format
    # Because it's string, sort properly (if needed)
    # For proper chronological sorting, convert back to date for sorting:
    def parse_date(date_str):
        try:
            return pd.to_datetime(date_str, format='%d.%m.%y')
        except:
            return pd.NaT

    df['ParsedDate'] = df['Date'].apply(parse_date)
    df = df.dropna(subset=['ParsedDate'])
    df = df.sort_values(by='ParsedDate')
    df = df.drop('ParsedDate', axis=1)

    # Save to Excel
    df.to_excel('emails.xlsx', index=False, engine='openpyxl')

if __name__ == '__main__':
    main()
