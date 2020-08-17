# 不定長度參數
def sum01(*m,**n):  # *可變的參數串列 , **可變的字典列表 涵義不同，順序不可對調
    print(m)
    print(n)

sum01(1,2,3)
sum01(a=10,b=20,c=30)
sum01(1,2,3,a=10,b=20,c=30)
# sum01(a=10,b=20,c=30,1,2,3)  # 格式不符合無法執行

print(sum([10,20]))  # 原始sum函數用法

# 一級函式可修改名稱
print(type(sum01))
s = sum01
print(s(5,6,7))