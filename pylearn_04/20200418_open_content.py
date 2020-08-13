# open 以各種模式開啟/寫入檔案
import os

#準備好文本 / py多行文字的寫法 內文須以三單引號夾起
content = '''
Sherly 跟 Eddie 兩個人在差不多的時間都從 Git Server 上拉了一份資料下來準備進行開發。
Sherly 手腳比較快，先完成了，於是先把做好的成果推一份上去。
Eddie 不久後也完成了，但當他要推上去的時候發現推不上去了…
via https://gitbook.tw/chapters/github/fail-to-push.html
'''
# open的 w模式
'''
f = open("xyz.txt","w")  
f.write(content)
f.close()
'''

# a模式
'''
f = open("xyz.txt","a")  
f.write(content)
f.close()
'''

# with ... as (可不使用close) 最推薦寫法  class 11 / ch 4.2.1
with open("uvw.txt","w") as f:
 f.write(content)

# encoding 不同編碼格式的處理方式
content2 = '''
如何尋找政治平衡
วิธีหาสมดุลทางการเมือง
Làm thế nào để tìm một sự cân bằng chính trị
'''

with open("rst.txt", "w", encoding="utf-8") as f:
 f.write(content2)

