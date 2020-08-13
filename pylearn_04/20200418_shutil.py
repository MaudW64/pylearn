# shutil 複製、搬移、刪除檔案
import os, shutil

sourcefile = input("複製並移除檔案：")
descfile = "xyz.py"

shutil.copy(sourcefile, descfile)  # 複製為新檔案
shutil.rmtree(sourcefile)  # 移除指定檔案
# shutil.rmtree("資料夾名稱")
