import os
import base64
import re
import pandas as pd
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email.utils import parsedate_to_datetime
from google.auth.transport.requests import Request

# Scopes and Credential files
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
    sender_email = ''
    for header in headers:
        if header['name'] == 'Subject':
            subject = header['value']
        if header['name'] == 'Date':
            date_str = header['value']
        if header['name'] == 'From':
            sender_email = header['value']  # contains full name + email

    # Extract only email address from "From" header
    import email.utils
    sender_email_parsed = email.utils.parseaddr(sender_email)[1]

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

    return subject, message_body, date_formatted, sender_email_parsed

def main():
    service = authenticate_gmail()
    keywords = ['received your application',
                'Thank you for your interest',
                'Thank you for submitting your application',
                'Thank you for your application',
                'vielen Dank für dein Interesse',
                'Your application',
                "your application has been received",
                'thank you again for applying',
                'received your application',
                'vielen Dank für deine Nachricht',
                'vielen Dank für die Zusendung',
                'vielen Dank für Ihre Bewerbung',
                'vielen Dank für Ihre Zusendung',
                'vielen Dank für Ihre Nachricht',
                'danken Ihnen für Ihre Bewerbung',
                "Ihre Bewerbung ist eingegangen",
                'möchten uns ganz herzlich für deine Bewerbung',
                'für deine Bewerbung' ]  # Adjust keywords as needed
                
    email_data = []

    for keyword in keywords:
        print(f"Searching for keyword: {keyword}")
        messages = search_emails(service, keyword)
        for msg in messages:
            subject, message, date, sender_email = get_email_details(service, msg['id'])
            email_data.append({
                'Date': date,
                'Email Title': subject,
                'Message Content': message,
                'Email Sender': sender_email
            })

    # Create DataFrame
    df = pd.DataFrame(email_data)

    # Remove entries without date for sorting
    df = df[df['Date'].astype(bool)]  # Remove empty date entries

    # Parse date for sorting
    def parse_date(date_str):
        try:
            return pd.to_datetime(date_str, format='%d.%m.%y')
        except:
            return pd.NaT
    df['ParsedDate'] = df['Date'].apply(parse_date)
    df = df.dropna(subset=['ParsedDate'])

    # Sort by parsed date
    df = df.sort_values(by='ParsedDate')
    df = df.drop('ParsedDate', axis=1)

    # Save to Excel
    df.to_excel('emails.xlsx', index=False, engine='openpyxl')


if __name__ == '__main__':
    main()



