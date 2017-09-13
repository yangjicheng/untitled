#coding:utf-8
import requests

#url = "http://www.owhat.cn/shop/shopdetail.html?id=444etertrt"
url = "http://www.owhat.cn/dgdgfgf"


try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])

except:
    print("失败")


