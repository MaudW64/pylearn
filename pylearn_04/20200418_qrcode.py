#製作qr用套件
import qrcode as g

img = g.make("http://aaron0117.blogspot.com/2008/08/strftime.html")
img.save("qr01.jpg")
img = g.make("https://gitbook.tw/chapters/using-git/amend-commit2.html")
img.save("qr02.jpg")

"""
img.show("qr.jpg")

#  INFO:
#  https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/565697/
"""