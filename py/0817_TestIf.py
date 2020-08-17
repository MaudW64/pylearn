# 判斷輸入文字/數字，並判斷成績的if判斷式
"""
# 文字/數字判斷 isnumeric() 範例
print('hello'.isnumeric())  # Fales
print('62'.isnumeric())  # True，數字(正整數)則返回 True 
print('72.9'.isnumeric())  # Fales
print('十'.isnumeric())  # True，一二三四五六七八九十皆為True

# string.isdigit() 如果 string 只包含數字(正整數)則返回 True 否則返回 False

# string.isdigit() 如果 string 只包含數字(正整數)則返回 True 否則返回 False

# isinstance(string, (type, type...))  判斷string是否為某種type

"""

strscore = input('請輸入整數成績：')
score = 0
if not isinstance(1, (int, float)):
    print('請輸入整數數字。')
else:
    score = float(strscore)
    if score > 100 or score < 0:
        print('請輸入0 ~ 100之間的數字。')
    elif score >= 90:
        print('厲害！得到 A。')
    elif score >= 80:
        print('好耶！得到 B。')
    elif score >= 70:
        print('不錯喔！得到 C。')
    elif score >= 60:
        print('還行。得到 D。')
    elif score < 60:
        print('不及格！得到 F。')
