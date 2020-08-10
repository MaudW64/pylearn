a = 60
b = 3.14
c = False
d = 'Hello'

print(a)
print(type(a))

print(b)
print(type(b))

print(c)
print(type(c))

print(d)
print(type(d))

print('Nick\'s jacket')

print('C:\\workspace\\tcfst')

print(r'C:\\workspace\\tcfst')

print(r'C:\workspace\tcfst')

print('\101')  #101 = A 的 8進位

'''
python 沒有實際意義上的多行註解，
此為沒有被print或執行功能的字串
'''

print(ord('A'))  #ASCII Code，用來檢查文字[a-z],[A-Z]
print(ord('z'))
print(ord('9'))
print(ord('可'))

print('Go','Home') #預設sep為一個空格
print('Go','Home', sep='')

a=10
b=3
print('%d除以%d得到%6.2f' %(10,3,10/3))
print('%d除以%d得到%.2f' %(a,b,a/b))
print('{}除以{}得到{:.2f}' .format(a,b,a/b))
print('{0}除以{1}得到{2:5.2f}' .format(a,b,a/b))

exit()