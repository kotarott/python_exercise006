import gspread
from oauth2client.service_account import ServiceAccountCredentials

JSON_PATH = 'keys/python-exercise006-9a62bfa12ed8.json'
SHEET_NAME = 'test_python'

# スプレッドシートとの接続
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_PATH, scope)
gc = gspread.authorize(credentials)
worksheet = gc.open(SHEET_NAME).sheet1

# スプレッドシートの読み書き
worksheet.update_acell('A1', 'Hello World!')
print(worksheet.acell('A1'))