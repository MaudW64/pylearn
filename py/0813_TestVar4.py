# 索引切片
text = 'Hello'
"""

     H  e  l  l  o
    0  1  2  3  4  5

     H  e  l  l  o
   -5 -4 -3 -2 -1 0 

"""
print('01',text[0:2]) # = text[:2]
print('02',text[3:5]) # = text[3:]
print('03',text[2:4])
print('04',text[:-3])
print('05',text[-4:-1])

# [start:end:step]
print('06',text[1:3:1])
print('07',text[:4:2])
print('08',text[::-1])  # 逆排

# 淺層複製
num1 = [10, 20, 30, 40, 50]
num2 = [60, 70, 80, 90, 100]
tlp1 = (num1 , num2)
tlp2 = tlp1[:]
print(tlp1)
