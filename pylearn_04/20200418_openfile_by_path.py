# 用os.path方法建立檔案
import os


fn = (input("請輸入檔名："))
cont = '''import os, system
# 開始輸入文字

'''

if not os.path.exists(fn):
    """
    #  寫法1 一般
    f = open(fn,"w")  # 檔名, 模式(w=覆蓋、r=讀取(預設)、a=附加)
    f.close()
    """
    # 寫法2 新建檔案內包含文字(cont)
    f = open(fn, "w" , encoding="utf-8")
    f.write(cont)
    f.close()
else:
    print("檔案已存在")