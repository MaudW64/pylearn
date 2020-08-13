# 邏輯運算
print((3>5) and (5>2))

# 複合指定運算子
i = 5
i += 10
print(i)
i **= .5  #指數運算
print(i)

# 進階.format 函式
print("{}今年{}歲".format("小明",25))
print("{name}今年{age}歲".format(name="小明",age=25))  #定義變數並引用，但離開此行後定義就消失無效
print("{age}歲的上班族，名為{name}。".format(name="小明",age=25))   #命名後可跳用

print("{0}今年{1}歲".format("小明",25))  #依照輸入順序作引數 (以 0 為第一個)
print("{1}歲的上班族，名為{0}。".format("小明",25))  #依照輸入順序作引數，可跳用

#判斷式
chi=int(input("請輸入中文成績："))
eng=int(input("請輸入英文成績："))
mat=int(input("請輸入數學成績："))
avg=(chi+eng+mat)/3

print("\n平均成績：",round(avg,1))

if(chi>=90):
    print("中文成績卓越！")
if(eng>=90):
    print("英文成績卓越！")
if(mat>=90):
    print("數學成績卓越！")
else:
    print("")
