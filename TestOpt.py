x = 7

print(x> 3)
print(x>=3)
print(x< 10)
print(x<=10)
print(x==3)
print(x!=3)

x = 3      # = 一個等號是"給值"
print(x==3)# ==兩個等號是"是否相等"

print('0<x<10=',0<x<10)
print('0<x<10=',0<x and x<10)
x+=1 # x=x+1
print(x)

y = 5
print(y+1)
#y = (y+1)
y += 1 # y=y+1
print(y)

print('5<x<10=',5<x and x<10) #and 一者為False則全為False
print('5<x<10=',5<x  &  x<10) 

print('x<5或10<x=',x<5  or 10<x) #or  一者為True 則全為True
print('x<5或10<x=',(x<5)| (10<x))#& | 是位元運算，不適合作邏輯運算(True/False)


print(bool([1]))
