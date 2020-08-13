# 製作函式(function)
"""
# 不須回傳的function
def pl01():
    print("**********")

print(input("輸入任意鍵建立 ***星型分隔線*** ："))
pl01()
"""
# 需回傳的function - 公英換算
def i2m(num_01):  # 英->公
    float(num_01)
    num_02 = num_01 * 25.4
    return num_02

num = float(input("輸入長度(mm)："))
print(i2m(num))