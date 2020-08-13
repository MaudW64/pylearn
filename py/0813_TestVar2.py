# Q2小數點問題解 decimal
# 0.1 在python的意涵 與 解決小數點的辦法
# from...import 的用法

import decimal
# from decimal import Decimal

n1 = 0.1
n2 = 0.2
d1 = decimal.Decimal(0.1)
# d1 = Decimal(0.1)
d2 = decimal.Decimal(0.2)
# d2 = Decimal(0.2)

print(n1+n2)  # 0.1 在python的意涵  -> 0.1在計算機內部的存儲是用二進位表示的
print(d1+d2)
print(d1)
print(type(d1))

d1 = decimal.Decimal('0.1')  # 解決方式 加單引號''作為字串
d2 = decimal.Decimal('0.2')

print(n1+n2)
print(d1+d2)
print(d1)
print(type(d1))
