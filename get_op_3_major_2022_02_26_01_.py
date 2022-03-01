import bs4
import csv
import datetime
import io
import json
import pandas
import requests
import time

def op3_df(y, m, d):
    url = "https://www.taifex.com.tw/cht/3/callsAndPutsDate"
    c_id = "TXO"
    q_date = str(y) + "/" + str(m) + "/" + str(d)
    payload = {
            "queryType": 1,
            "doQuery": 1,
            "commodityId": c_id,
            "queryDate": q_date
            }
    response = requests.get(url, params = payload)
    soup = bs4.BeautifulSoup(response.text, "lxml")
    tables = soup.select("table")
    '''確認當日是否有資料'''
    t_check = pandas.read_html(tables[2].prettify())
    df = []
    if len(t_check) > 0:
        dfs_check = t_check[0]
        if dfs_check.iat[0, 1] != "查無資料":
            table = pandas.read_html(tables[3].prettify())
            data_frames = table[0]
            for i in range(3, 9):
                df.append(
                    [y, m, d,
                     data_frames.iat[i, 2], data_frames.iat[i, 3],
                     data_frames.iat[i, 4], data_frames.iat[i, 5],
                     data_frames.iat[i, 6], data_frames.iat[i, 7],
                     data_frames.iat[i, 10], data_frames.iat[i, 11],
                     data_frames.iat[i, 12], data_frames.iat[i, 13]
                     ]
                    )
    return df
def load_data(y1, m1, d1, y2, m2, d2):
    if (y1, m1, d1) < (y2, m2, d2):
        y1, m1, d1, y2, m2, d2 = y2, m2, d2, y1, m1, d1
    d_start = datetime.date(y1, m1, d1)
    d_end = datetime.date(y2, m2, d2)
    data = []
    while d_start >= d_end:
        y, m, d = d_start.year, d_start.month, d_start.day
        print(y, m, d)
        df = op3_df(y, m, d)
        if df != []:
            for d in df:
                data.append(d)
        d_start = d_start - datetime.timedelta(days = 1)
    return data

def write_to_csv(y1, m1, d1, y2, m2, d2):
    with open("op_3_data.csv", "w", newline = "") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(
            ["Year", "Month", "Day",
             "C/P", "3_Major",
             "V_B_lot", "V_B_amount",
             "V_S_lot", "V_S_amount",
             "OI_B_lot", "OI_B_amount",
             "OI_S_lot", "OI_S_amount",
             ]
            )
        for d in load_data(y1, m1, d1, y2, m2, d2):
            csv_writer.writerow(d)

t_tag = time.time()
write_to_csv(2022, 2, 26, 2019, 1, 1)
print(time.time() - t_tag)