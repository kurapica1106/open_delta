import requests

url = "https://www.taifex.com.tw/cht/3/futContractsDate"
form_data = {}
r = requests.post(url, data = form_data)
print(r.text)