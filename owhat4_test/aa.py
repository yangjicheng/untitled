#-*- coding:utf-8 -*-
from login import *
import xlrd
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
# 打开owhat网站
login("13123456789","111111")
time.sleep(1)
nowhandle=browser.current_window_handle
browser.find_element_by_xpath("html/body/section[5]/div[1]/div[2]/ul/li[1]/a/span").click()
time.sleep(1)
browser.find_element_by_xpath("html/body/section[5]/div[1]/div[2]/ul/li[1]/ul[1]/li/a").click()
time.sleep(1)
browser.find_element_by_xpath("html/body/section[5]/div[2]/section/section/header/a").click()
time.sleep(5)
#获取所有窗口
allhandles=browser.window_handles
#判断窗口是否当前窗口
for handle in allhandles:
   if handle != nowhandle:
       browser.switch_to_window(handle)
# 滚动页面
time.sleep(1)
js="var q=document.body.scrollTop =10000"
browser.execute_script(js)
time.sleep(1)
browser.find_element_by_xpath("html/body/section[5]/div[2]/form/section/section[3]/div[1]/div[4]/div/div[1]/button").click()
time.sleep(1)
browser.find_element_by_xpath("html/body/div[2]/div/div/div/div[2]/form/div[2]/div/input").send_keys(11)