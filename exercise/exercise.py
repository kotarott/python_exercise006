import requests
import json

url = "https://www.googleapis.com/books/v1/volumes?q="

def main(book_name):
    req_url = url + book_name
    response = requests.get(req_url)
    items = json.loads(response.text)["items"]
    book_names = []
    for item in items:
        book_info = item["volumeInfo"]
        book_names.append(book_info["title"])
    return book_names

if __name__ == "__main__":
    book_name = input("検索ワードを入力してください。")
    print(main(book_name))