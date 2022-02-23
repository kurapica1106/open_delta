import bs4
import io
import json
import pandas
import requests

y = 2022
m = 2
d = 21
url = "https://www.taifex.com.tw/cht/3/futDailyMarketReport"
data = {
        "marketCode": 1,
        "commodity_id": "TX",
        "queryDate": f"{y}%2F{m}%2F{d}"
        }

response = requests.get(url, data = data)

soup = bs4.BeautifulSoup(response.text, "lxml")


tables = soup.find_all("table")
table_bodys = tables[4].find_all("tbody")

table_heads = table_bodys[0].find_all("th")
for head in table_heads:
    print(head.text)

table_datas = table_bodys[0].find_all("td")
for data in table_datas:
    print(data.text)
