# list (append,insert,remove), set (add),
"""
s = [10,20,30]
print(s)
print(type(s))
print(s[0])
print(s[1])
print(s[2])

s.append(40)
print(s)
s.insert(2,10)
print(s)
s.remove(20)
print(s)

"""
t = {10,30,20}  # set 用大括弧 (類似dict但沒有key跟冒號  dict01 = {id_01 : apple})
print(t)
print(type(t))

t.add(25)  # set加入元素必須用add(不可用append,insert), 加入的元素順序沒有一定, set元素可用remove移除
print(t)
t.remove(20)
print(t)

t2 = list(t)  # set轉list
print(t2)
print(type(t2))
