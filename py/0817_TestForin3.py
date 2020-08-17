# 99乘法表
for m in range(1,10):
    for n in range(2,7):
        print(n,'x',m,'=',m*n,sep='',end='')
        print('\t',end='')
    print('\n')