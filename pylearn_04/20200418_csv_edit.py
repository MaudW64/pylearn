# 編輯資料庫(csv)
import csv
with open("新北市公共自行車租賃系統01.csv","r",encoding='utf-8-sig') as cfile:
    patten = list(csv.reader(cfile))
    print(patten)
