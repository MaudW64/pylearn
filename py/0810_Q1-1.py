# 不使用 in 的描述方式

a=input('請輸入文字01: ')
b=input('請輸入文字02: ')
c=input('請輸入文字03: ')
s = [a,b,c]
d='海'
count = 0
TaF=False

while count < len(s):    
    if d!=s[count]:       
       count += 1
    else:
        count += 1
        TaF=True
        print('結果包含',d,', 且位於資料第',count,'欄。')
    
if TaF==False :
    print('結果是否包含',d,'：',TaF)