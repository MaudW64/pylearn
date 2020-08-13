# type的練習 + 參數格式化( %() 與 .format )用在print的練習
'''
name = "Maud"
health = 746.567
nstr = 20
nint = 18
nluk = 44

#參數格式化 by %()
print("%s is your character\'s name. \t %s will start their travel." %(name, name))  # %()  參數格式化，一個蘿蔔一個坑的概念
print("%s is your character\'s name. \t %s will start their travel." %(name, name), end=" ...\n=================\n") 
print("%s \'s health is %d." %(name, health))  # %()內填入的變數需要1.依出現順序排列、2.宣告+前面句子的type相符(浮點與整數可互換)，不然會出錯
print("health is %d, %s is alive." %(health, name))
print("health is %5d, %5s is alive." %(health, name)) # %5d  整數固定為5位數(沒有數值則用空白補上)
print("health is %8.2d, %5s is alive." %(health, name)) # %8.2f  數固定為8位數(包含小點+小數)(沒有數值則用空白補上)，小數點捨入至後二位，但%d強制捨去小數，故不顯示
print("health is %s, %s is alive." %(health, name))
print("health is %f, %s is alive." %(health, name))
print("health is %.2f, %s is alive." %(health, name))  # %.2f  小數點捨入至後二位
print("health is %6.8f, %s is alive." %(health, name))  # %6.8f  數固定為14位數(包含小點+小數)(沒有數值則用空白補上)，小數點捨入至後八位
print("health is %2.8f, %s is alive." %(health, name))  # %2.8f  數固定為二位數(包含小點+小數)(超過則不補空白)，小數點捨入至後八位

#參數格式化 by format
print("力量：%d、法力：%d、運氣：%d" %(nstr, nint, nluk))  #參數格式化 by %()，對照組
print("力量：{}、法力：{}、運氣：{}".format(nstr, nint, nluk))  #參數格式化 by format，類似 %() 但優點是不須再前面句子定義變數type

# round 四捨五入 (不是小數捨去)
pi=3.141592653589
print("pi is ",pi , end=".\n")
print("pi is ",round(pi,3) , end=".\n") 
print("pi is ",round(pi,4) , end=".\n") 
print("pi is ",round(pi,5) , end=".\n") 
print("pi is ",round(pi,6) , end=".\n") 
'''

# 變數type辨別與轉換
# 轉換成int  int(變數名稱)
# 　　float  float(變數名稱)
# 　　string  str(變數名稱)

# 用油量與油價計算
kl = input("輸入公升數: ")  # 變數kl被系統默認為 字串，導致無法無法做後續浮點數運算
print(type(kl))  # 檢測變數kl的type
print("================")
kl=float(kl)
print(type(kl))  # 修改type後，再次檢測變數kl的type

oil_price = 21.8 #2020.03.21 95價格
cal = oil_price * kl
print("您共需付{}元，謝謝您的惠顧~" .format(cal))
print(type(cal))

exit()