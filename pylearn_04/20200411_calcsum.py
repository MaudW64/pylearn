#  不定數目參數函數 class6 / ch3.3.2
#  星字號(可變長度串列/元組/字典) 見：
#  https://e8859487.pixnet.net/blog/post/403127384-%5Bpython%5D-%2A%2A-%E9%9B%99%E6%98%9F%E8%99%9F%28double-star-asterisk%29-vs-%2A%E5%96%AE%E6%98%9F%E8%99%9F%28st

def calcsum(*p1):
    total = 0
    for x in p1:
        total+=x
    return total

a = calcsum(6,15)
b = calcsum(4,5,7)
c = calcsum(1,2,3,4,5)
d = calcsum(12,5,33)
print(a,b,c,d)
