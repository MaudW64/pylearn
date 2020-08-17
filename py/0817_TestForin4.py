# for in 的精簡寫法
"""
s=[]
for n in range(5):
    s.append(n**2)
print(s)
"""

print([n**2 for n in range(5)])  # 注意中括弧

"""
print(tuple(n+1 for n in range(49)))
"""

# if else 精簡寫法
num = 19
"""
if num%2:  #等同於num%2==1，因 判斷式結果為1 -> 直接轉換為true (0->false)
    print('奇數')
else:
    print('偶數')
"""

print('奇數' if num%2 else '偶數')

# for in + if else 精簡寫法
"""
s=[]
for n in range(10):
    if n%2:
        s.append(n**2)
print(s)
"""

"""
odd=[n**2 for n in range(10) if n%2]
print(odd)
"""

print([n**2 for n in range(10) if n%2])
