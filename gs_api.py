import gspread
from oauth2client.service_account import ServiceAccountCredentials
import rakuten_api as rakuten
from common.spread_sheet_manager import SpreadsheetManager
import pandas as pd

JSON_PATH = 'keys/python-exercise006-9a62bfa12ed8.json'
SHEET_NAME = 'test_python'

def connect_gs_by_sheetname(sheet_name):
    # スプレッドシートとの接続
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_PATH, scope)
    gs = gspread.authorize(credentials)
    worksheet = gs.open(sheet_name).sheet1
    return worksheet

# スプレッドシートの読み書き
# worksheet.update_acell('A1', 'Hello World!')
# print(worksheet.acell('A1'))

def main():
    ss = SpreadsheetManager()
    ss.connect_by_sheetname(SHEET_NAME)
    # ss.test()
    df = rakuten.search_items("チーズケーキ")
    # print(type(df))
    ss.insert_by_df(df)

if __name__ == "__main__":
    main()