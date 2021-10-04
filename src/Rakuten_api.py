import os

import requests
from dotenv import load_dotenv

load_dotenv()
requests_url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20\
170706"

# serch_keyword = (input("検索したいキーワードを入力してください。>>"))
serch_keyword = input("")
serch_params = {
    "format": "json",
    "keyword": serch_keyword,
    "applicationId": os.environ["APP_ID"],
    "hits": 30,
    "page": 1,
}

response = requests.get(requests_url, serch_params)
result = response.json()
print(result)
