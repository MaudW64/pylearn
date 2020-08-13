# for迴圈, break ,continue

# 挑出12號
for i in range(1,16):
    if(i==12):
        print(str(i)+"/", end="\n")    
    else:
        print(i)


# 休息日
for i in range(1,32):
    if(i%7==6 or i%7==0):
        print(str(i)+"休息日", end="\n")    
    else:
        print(i)


# continue - 不要4
for i in range(1,13):
    if(i==4):
        continue
    else:
        print(i)
print("\a")

"""

# 日期工具 datatime
import datetime as dt
from dateutil.rrule import rrule, DAILY

start_date = dt.date(2020,3,1)
end_date = dt.date(2020,3,31)

for x in rrule( DAILY, dtstart=start_date, until=end_date):
    a = dt.date.isoweekday(x)
    b = x.strftime("%Y%m%d")
    if(a==6 or a==7):
        continue
    if(b=='20200316'):
        break
    print(b,a)

"""