"""
# while
piece = 1
total = 0
while (piece>=0):  #輸入小於0的數字時 跳出迴圈
    piece = float(input("輸入數量，若要加總，則輸入任意負數:"))
    total = total + piece
    print("目前加總：", total)
input("程式已結束，按任意鍵離開。")
"""
# for vs while
x1=4
a1=0
b1=0
while(b1<x1):
    b1+=1
    print(b1,a1)

x2=4
a2=0
b2=0
for x2 in range(x2):
    b2+=1
    print(b2,a2)