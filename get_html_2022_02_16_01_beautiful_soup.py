import bs4
import requests

url = "https://www.taifex.com.tw/cht/3/futContractsDate"
form_data = {}
response = requests.post(url, data = form_data)
obj_soup = bs4.BeautifulSoup(response.text, "lxml")
print(obj_soup.find_all("TR"))