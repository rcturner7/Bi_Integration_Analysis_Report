# This application uses comments of code providing what it would look like if using Zendesk
# using requests is a library for using API's like Zendesk
# import requests
import os
from dotenv import load_dotenv
import pandas as pd
from pymongo import MongoClient

# Initialize variables
read_tickets = None
collection = None

# ZenDesk API setup (Commenting this part out since this project is for practice, but wanted to show
# what the code can look like to give developers an idea on building bi/analyst applications using
# real-world applications.
# zendesk_api = 'https://yourcompany.zendesk.com/api/v2/tickets.json'
# api_token = 'your_api_token'
# headers = {'Authorization': f'Bearer {api_token}'}

# Fetch data from ZenDesk
# response = requests.get(zendesk_api, headers=headers)
# tickets = response.json()['tickets']

load_dotenv()  # This loads the variables from .env

# Environment variables for security
atlas_uri = os.environ.get('MONGO_ATLAS_URI')
db_name = 'Customer_Support_Tickets'

# Read CSV file for practice of customer support tickets instead of using zendesk API
try:
    read_tickets = pd.read_csv('zendesk_tickets.csv')
except Exception as e:
    print("Error reading CSV file:", e)
    exit()

# MongoDB setup
if read_tickets is not None:
    try:
        client = MongoClient(atlas_uri)
        db = client[db_name]
        collection = db.zendesk_tickets
    except Exception as e:
        print("Error connecting to MongoDB:", e)
        exit()

# Insert data into MongoDB
if collection is not None and read_tickets is not None:
    try:
        collection.insert_many(read_tickets.to_dict('records'))
    except Exception as e:
        print("Error inserting data into MongoDB:", e)
