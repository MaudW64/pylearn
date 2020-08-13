# List、Dict新增元素； tumple 與 python可自動拆解tuple (unpack)
"""
ss = []
s1 = input('輸入字串01：')
ss.append(s1)
s2 = input('輸入字串02：')
ss.append(s2)
s3 = input('輸入字串03：')
ss.append(s3)
q = input('查詢字串：')
print(q,'存在',ss,'資料中：',q in ss)
"""

"""
data = {'Lang':'Python','Version':3.8}
print(data)
print(type(data))
print(data['Version'])  # ['key'] 要用中括弧
print('Lang' in data)
data['Os'] = 'Windos'  # 增加dict的元素
print(data)

del data['Version']
print(data)

print('R' in data)
print('R' in data.values())  # 兩句意義不同
print('Lang' in data.keys())
print('Lang' in data.items())

a,b = data  # unpack, unpack的數量必須跟dict的items數量一致
print('01',a)
print('02',b)

c,d = data.values()
print('03',c)
print('04',d)
"""

"""
dict = {'Name': 'Zara', 'Age': 7, 'Lang':'Python','Version':3.8}

print ('Value : %s' % dict.values())
print ('Value : {}' .format(dict.values()))
"""

"""
tup = (15,20,25)
print(tup)
print(type(tup))
print(tup[0])
print(tup[1])
print(tup[2])

x = 77
y = 66
x,y = y,x
print(x,y)

a, b, c = tup  # unpack, unpack的數量必須跟tuple元素數量一致
print(a)
print(b)
print(c)
"""

m, *n = (1, 2, 3, 4, 5)  # unpack拆解法2:使用星號*, 也可以用在list, set
print(m)
print(n)

m, *n, p = ('金', '木', '水', '火', '土')
print(m)
print(n)
print(p)
