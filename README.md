WhatsApp Message Sender + Smart Data Extractor
Overview

This project is a Playwright-powered WhatsApp Web Automation Bot developed as part of the Social Eagle Gen AI Architect Program assignment.

The bot automates customer communication by:

Logging into WhatsApp Web
Reading contacts from an Excel file
Sending personalized messages
Taking screenshots after sending messages
Extracting the latest messages from chats
Generating Excel and JSON reports
Features
Message Automation
Opens WhatsApp Web using Playwright
Supports manual QR code login on first run
Reads contacts from Excel
Replaces {name} placeholders with actual contact names
Sends personalized WhatsApp messages
Smart Data Extraction
Opens each chat after sending
Extracts the last 3 messages from the conversation
Stores extracted data for reporting
Reporting

Generates:

whatsapp_report_YYYY-MM-DD.json
whatsapp_report_YYYY-MM-DD.xlsx
Additional Features
Human-like delays (2–5 seconds)
Error handling
Screenshot capture
Status tracking for each contact
Tech Stack
Python
Playwright
Pandas
OpenPyXL
WhatsApp Web
Project Structure
project/
│
├── playwright_assign.py
├── contacts.xlsx
├── screenshots/
│
├── whatsapp_report_YYYY-MM-DD.json
├── whatsapp_report_YYYY-MM-DD.xlsx
│
└── README.md
Installation
Create Virtual Environment
python -m venv venv
Activate Virtual Environment

Windows:

venv\Scripts\activate
Install Dependencies
pip install playwright pandas openpyxl
Install Playwright Browser
playwright install chromium
Input File Format

Create a file named:

contacts.xlsx

with the following columns:

Name	Phone	Message
Vishva	919876543210	Hello {name}, welcome!
Aswin	919812345678	Hi {name}, thank you for connecting.
Notes
Include country code in phone number.
Do not use spaces.
Message templates can contain {name}.
Running the Project
python playwright_assign.py
First Run
WhatsApp Web opens.
Scan QR code manually.
Press Enter in the terminal.
Automation begins.
Output Generated
JSON Report

Example:

[
  {
    "name": "Vishva",
    "phone": "919876543210",
    "status": "SENT",
    "last_3_messages": [
      "Hello",
      "How are you?",
      "Thank you"
    ]
  }
]
Excel Report
Name	Phone	Status	Last 3 Messages
Vishva	919876543210	SENT	Hello | How are you? | Thank you
Screenshots

A screenshot is captured after every successful message send.

Example:

screenshot_Vishva_2026-06-23.png
Error Handling

The bot handles:

Invalid contacts
Contact not found
Missing message box
Network delays
WhatsApp loading issues

Failed contacts are marked in the report.

Assignment Requirements Covered
Playwright Automation
WhatsApp Web Login
Excel Input
Personalized Messages
Dynamic Waits
Random Delays
Message Extraction
Screenshot Capture
JSON Reporting
Excel Reporting
Error Handling
Single File Implementation
Author

Vishva Venkataraman
