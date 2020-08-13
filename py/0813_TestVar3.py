# 邏輯運算
"""
print(10+3)
print(10-3)
print(10*3)
print(10/3)
print(10%3)  # 餘數
print(10//3)  # 整除得商

print(2**3)  # 三次方
print(2**-1)
print(2**.5)  # 開根號

print('Hello'*5)
print([10,20,30]*3)
print([10,20,30]+[40,50])
"""

"""
x = 7
print(x>3)
print(x>=3)
print(x<10)
print(x<=10)
print(x==3)
print(x!=3)

# 位元運算
a=3
b=2
a<<=b  # a(二進位 0011)的位元左移2格 -> new a = 1100 = 十進位12
print(a)

print(3 & 7)  # & 進行位元運算，本質是計算數值
print(3 and 7)  # and 進行邏輯運算，本質是計算布林
"""

# set 交集聯集差集
users = {'abc','def','ghi'}
admins = {'AAA','BBB','abc'}

print('admins & users: ', admins & users)
print('admins | users: ', admins | users)
print('admins - users: ', admins - users)  # 差集
print('admins ^ users: ', admins ^ users)  # 互斥
print('admins > \'AAA\',\'BBB\': ', admins > {'AAA','BBB'})  # 前包含後
print('admins < \'AAA\',\'BBB\': ', admins < {'AAA','BBB'})  # 後包含前