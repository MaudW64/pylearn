# 排序sorted
from soupsieve.util import upper

data=[2,1,6,5,3,9]
print(sorted(data))

texts = ['aBCD','BcD','cD']
print(sorted(texts))  # sort 修改原變數; sorted 不修改原變數
print(sorted(texts,key=len))
print(sorted(texts,key=str.upper))

