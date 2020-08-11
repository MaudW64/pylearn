a='五'
b='正'
c='海'

s = [a,b,c]
d='海'

count = 0
while count < len(s):
    if d == s[count]:
    return(True)

print('結果：',d in s)