#各種path方法
import os

#完整路徑(for檔案)
text = os.path.abspath(__file__)  # __file__ 當前運行檔案
print("\n1. ",text)

#檔名/路徑(for檔案/路徑)
text = os.path.basename(__file__)
print("\n2. ",text)

# 路徑
text = os.path.dirname(__file__)  
print("\n3. ",text)