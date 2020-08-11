from sys import argv

s = [8, 16, 25, 72, 16 ,36]
print(s)
print(type(s))

print(s[0])
print(s[1])
print(s[2])

s.append(40)
print(s)

s.remove(16) #有一個以上的16，則刪除排序較前的16
print(s)

del s[1] 
print(s)

print(8 in s)