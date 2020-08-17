def sum01(nums):
    result = 0
    for i in nums:
        result += i
    return result

def max01(x1,x2):
    return x1 if x1>x2 else x2

data01 = [1,2,3,4,5,6,7,8,9,10]
print(sum01(data01))
data02 = [10,20,30,40]
print(sum01(data02))
data03 = [150,200,250]
print(sum01(data03))

print(max01(30,32))