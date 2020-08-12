from bs4 import BeautifulSoup
import requests

head_Html_lotto='http://www.taiwanlottery.com.tw/Lotto/Lotto649/history.aspx'
res = requests.get(head_Html_lotto, timeout=30)
print(res.text)
