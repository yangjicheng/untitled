
#-*- coding:utf-8 -*-
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(3)
browser.maximize_window()
time.sleep(3)
js="var q=document.body.scrollTop =10000"
browser.execute_script(js)
time.sleep(3)