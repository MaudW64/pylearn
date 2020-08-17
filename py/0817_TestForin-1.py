text='Python'

# 原始排列
for i,t in zip(range(1,len(text)+1),text):
    print(i,t)



# 逆向排列，參考 索引切片 0813_TextVar4
print(list(zip(list(range(1,len(text)+1))[::-1],text)))

for i,t in zip(list(range(1,len(text)+1))[::-1],text):
    print(i,t)
