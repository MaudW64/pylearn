# glob 以檔名搜尋
import glob as g

f=g.glob("*.py")  # 萬用字元 *
for x in f:
    print(x)