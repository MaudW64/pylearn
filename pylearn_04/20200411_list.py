# list, tuple, dict  & 修改方式(append、insert 與 extend)

# list (以中括弧顯示的資料串) 的建立與修改
stuff = ["黃","陳","劉","林"]
print(stuff)

while True:
    chioce = input("請輸入剔除的組員(或直接enter跳出)：")
    if(chioce==""):  # 不輸入內容直接enter的處理方式(跳出迴圈)
        break
    num = stuff.count(chioce)
    if(num>0):        
        stuff.remove(chioce)  #remove 移除list中的元素  append 新增list中的元素
        print(chioce,"已移除")
        print("尚有組員：",stuff)
    else:
        print("組員不存在")

stuff.insert(0,'盧')  #在stuf[0]加入(insert)'盧' ,其他項目向後推一格來排序
print(stuff)

"""
# Tuple 元組-小括弧, dict 字典-大括弧

word01 = ("東","南","西") # 元組(若不轉換成list)則無法修改
word02 = {"ASUS":30,"Apple":70,"Sony":45}

word02["HP"] = 65  # 在字典中添加新項目
print(word02)

word03 = list(word01)  # tuple → list
print(word03)  # 顯示為中括弧
word03.append("北")  # 添加新項目
word04 = tuple(word03)  # list → tuple
print(word04) # 顯示為小括弧(元組tuple)
"""