# for in, 一個以上的引數(i, t)
# 配合range, zip, enumerate

text='Python'  # for in 條件式對str視為list
s =[10,20,30,40,50,60]  # for in 條件式可為list set tuple
for d in s:
    print(d)

n = 1
for e in text:
    print(n, e)
    n += 1

# for in + range
"""
print(len(range(6)))
print(list(range(1,6)))
print(list(range(3,8)))
"""

for i in range(len(text)):
    print(i,text[i])

# zip
"""
print(list(zip(range(len(text)),text)))

for i,t in zip(range(len(text)),text):
    print(i,t)
"""

# enumerate
"""
print(list(enumerate(text)),end='\n\n')

for i,t in enumerate(text):
    print(i,t)

for row in enumerate(text):
    print(row[0],row[1])

for row in enumerate(text,4):  # enmuerate 默認從0起算, 可以指定開始數字
    print(row[0],row[1])
"""