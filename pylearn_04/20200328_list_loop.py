# 串列(list)
classmate_01 = [10,25,34,47,56]
classmate_02 = ["金","木","水","火","土"]
print(classmate_01[1])
print(classmate_02[0])
print(classmate_02[-2]) #索引值小於0,可逆向選值

# 隨機套件 ramdon
import random as pickup  # as "新陣列名稱"
print(pickup.sample(classmate_02,1),pickup.sample(classmate_01,2))  # "新陣列名.sample( 原資料陣列, 數量)"
input("按任意鍵繼續。")