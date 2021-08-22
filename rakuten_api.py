import requests
import urllib.parse
import pandas as pd
import os

APP_ID = "applicationId=[自分のID]"

def search_items(keyword):
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?"
    url += APP_ID
    set_keyword = "&keyword=" + urllib.parse.quote(keyword)
    url += set_keyword
    api_response = requests.get(url).json()
    item_name_price = []
    for item in api_response["Items"]:
        item_name_price.append([item["Item"]["itemName"], item["Item"]["genreId"], item["Item"]["itemPrice"]])
    df = pd.DataFrame(item_name_price, columns=["Name", "genreId", "price"])
    return df

def get_maxmin_price(keyword):
    url = "https://app.rakuten.co.jp/services/api/Product/Search/20170426?"
    url += APP_ID
    url += "&format=json"
    set_keyword = "&keyword=" + urllib.parse.quote(keyword)
    url += set_keyword
    api_response = requests.get(url).json()
    item_list = []
    for item in api_response["Products"]:
        item_list.append([item["Product"]["productName"], item["Product"]["genreId"], item["Product"]["maxPrice"], item["Product"]["minPrice"]])
    df = pd.DataFrame(item_list, columns=["Name", "genreId", "min_price", "max_price"])
    return df

def get_ranking(genre):
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?"
    url += APP_ID
    set_genreId = "&genreId=" + str(genre)
    url += set_genreId
    api_response = requests.get(url).json()
    item_list = []
    for item in api_response["Items"]:
        item_list.append([item["Item"]["rank"], item["Item"]["itemName"], item["Item"]["shopName"], item["Item"]["reviewCount"], item["Item"]["itemPrice"]])
    df = pd.DataFrame(item_list, columns=["rank", "Name", "Shop", "review_num", "price"])
    return df

def create_csv(data, file_name="items.csv"):
    num = 0
    while num == 0:
        if os.path.exists(file_name):
            print(f"ファイル名{file_name}は存在します。")
            num = 0
            file_name = input("ファイル名を入力してください >>>")
            file_name += ".csv"
        else:
            data.to_csv(file_name)
            return print("ファイルを作成しました。")

if __name__ == "__main__":
    df0 = search_items("チーズケーキ")
    create_csv(df0)
    # df1 = get_maxmin_price("スタンディングデスク")
    # create_csv(df1, "item_price_list.csv")
    # df2 = get_ranking(100283)
    # create_csv(df2)
    pass