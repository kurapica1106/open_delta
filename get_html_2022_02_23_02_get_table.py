import bs4
import io
import json
import pandas
import requests

url = "https://www.taifex.com.tw/cht/3/futDailyMarketReport"
m_code = 0
c_id = "TX"
y, m, d = 2022, 2, 21
q_date = str(y) + "/" + str(m) + "/" + str(d)
payload = {
        "marketCode": m_code,
        "commodity_id": c_id,
        "queryDate": q_date
        }
response = requests.get(url, params = payload)
soup = bs4.BeautifulSoup(response.text, "lxml")
tables = soup.select("table")
table = pandas.read_html(tables[4].prettify())
data_frames = table[0]
print(data_frames.iat[0, 1])
data_frames.to_csv("test.csv", encoding = "utf_8_sig")