
# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# 访问百度
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)
driver.maximize_window()
driver.execute_script("window.scrollBy(0,200)","")
time.sleep(3)