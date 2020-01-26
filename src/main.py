import configparser
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from monzo import Monzo

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

config = configparser.ConfigParser()
config.read('config/config.ini')

creds = ServiceAccountCredentials.from_json_keyfile_name("config/creds.json", scope)
client = gspread.authorize(creds)

doc = client.open("Goals")
worksheet_list = doc.worksheets()
worksheet = doc.worksheet("Finance")

data = worksheet.get_all_records()

print(data)

# Monzo
print(config.get('API', 'apikey'))
client = Monzo(config.get('API', 'apikey')) # Replace access token with a valid token found at: https://developers.monzo.com/
account_id = client.get_first_account()['id'] # Get the ID of the first account linked to the access token
balance = client.get_balance(account_id) # Get your balance object
print(balance['balance']) # 100000000000
print(balance['currency']) # GBP
print(balance['spend_today']) # 2000
transactions = client.get_transactions(account_id, "2020-01-25T23:00:00Z", "2020-01-01T23:00:00Z", 10)
print(transactions)

# config.get('API', 'apikey')
#path_items = config.items( "paths" )
# for key, path in path_items:


# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
# pip install gspread oauth2client



