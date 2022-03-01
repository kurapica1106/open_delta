import csv
import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()
csv_file = open(r"D:\Python\open_delta-get_html\抓好的資料\op_day_data.csv")
rows = csv.reader(csv_file)
sql = "insert into test values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
cur.executemany(sql, rows)
con.commit()
con.close()