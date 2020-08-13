# 開始輸入文字
import os, csv
# cvs read
with open('新北市公共自行車租賃系統02.csv','r',encoding='utf-8') as csvfile:

    #  cvs.reader(csvfile)
    nlist = list(csv.reader(csvfile))
#print(nlist,sep='\n',end='--------')

pr = 1
for pr in nlist:
    print(nlist[pr],end='\n')
    pr+=1


