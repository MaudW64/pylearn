#刪除檔案remove、新增路徑mkdir、移除路徑rmdir

import os

files = input("輸入檔名(含附檔名)：")
if os.path.exists(files):
    os.remove(files)
    print("已刪除檔案。")
else:
    print("No File.")