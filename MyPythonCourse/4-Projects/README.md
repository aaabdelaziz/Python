# Email Survey Script

## Overview
This Python script allows you to search through your Gmail emails for specific keywords, extract relevant email information, and generate an Excel sheet containing the email date, title, and message content. This tool is useful for email surveys, analysis, or keyword-based email filtering.

---

## Features
- Authenticate with your Gmail account via OAuth 2.0.
- Search emails based on user-defined keywords.
- Extract email subject, message content, and date.
- Generate an Excel report with the filtered emails for further review or analysis.

---

## Prerequisites
- Python 3.x installed on your system.
- Google Cloud project with Gmail API enabled.
- Necessary Python libraries installed (`google-auth`, `google-auth-oauthlib`, `google-api-python-client`, `pandas`, `openpyxl`).

---

## Setup Instructions

### 1. Create Google Cloud Project & Enable Gmail API
- Visit [Google Cloud Console](https://console.developers.google.com/).
- Create a new project or select an existing one.
- Enable the Gmail API:
  - Navigate to **APIs & Services > Library**.
  - Search for **Gmail API**.
  - Click **Enable**.

### 2. Create OAuth 2.0 Credentials
- In **APIs & Services > Credentials**:
  - Click **Create Credentials > OAuth client ID**.
  - Choose **Desktop app**.
  - Download the generated `credentials.json` file.
- Save the `credentials.json` file in the same folder as the script.

### 3. Install Required Libraries
Run the following command to install the required Python libraries:
```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib pandas openpyxl
