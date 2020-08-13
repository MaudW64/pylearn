# range (以樂透號碼為例)
lotto_list01 = range(1,50)
print(lotto_list01)

# range (以樂透號碼為例) part02
import random as r

lotto_list02 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20, \
    21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,28,39,40, \
    41,42,43,44,45,46,47,48,49]
    # 在括弧內可用 \ 換行，用於過長的文字 
print(lotto_list02)
print(r.sample(lotto_list02,6))

# for迴圈
for Num in lotto_list01:
    print(Num, end="\n")

text01="以下所有內容是我在五倍紅寶石學院 Git 培訓教學課程\
    以及 Git 線上教學課程「人生不能重來，但 GIT 可以」所用到的教材，\
    若您發現內容有誤或有任何問題，歡迎直接來信"

count = 0

for findG in text01:
    if(findG=="G"):
        print(findG, end="")
        count=count+1
    else:
        print("-", end="")

print("\n",count)