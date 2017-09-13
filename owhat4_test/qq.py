#-*- coding:utf-8 -*-
#-*- coding:utf-8 -*-
from login import *
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from launch import launch
#launch("4","aaaaaa","D:\\2.png","description","o","11","o","2017-07-05 12:19:00","2017-07-23 07:03:00","8","58","0.01","leixing","111","1","11")
login("13123456789","111111")
time.sleep(1)
nowhandle = browser.current_window_handle
time.sleep(1)
browser.find_element_by_xpath("html/body/section[5]/div[1]/div[2]/ul/li[1]/a/span").click()
time.sleep(1)
browser.find_element_by_xpath("html/body/section[5]/div[1]/div[2]/ul/li[1]/ul[1]/li/a").click()
time.sleep(1)
#browser.find_element_by_xpath("html/body/section[5]/div[2]/section/section/header/a").click()
time.sleep(1)
browser.find_element_by_xpath("html/body/section[5]/div[2]/section/section/div[2]/div/div[2]/div/div[2]/table/tbody/tr[2]/td[14]/div/a").click()
time.sleep(1)
browser.find_element_by_xpath("html/body/section[5]/div[2]/section/section/div[2]/div/div[2]/div/div[2]/table/tbody/tr[2]/td[14]/div/div/div/a[1]").click()
time.sleep(2)
# 获取所有窗口
allhandles = browser.window_handles
# 判断窗口是否当前窗口
for handle in allhandles:
    if handle != nowhandle:
        browser.switch_to_window(handle)
time.sleep(1)

b = browser.find_element_by_xpath("html/body/section[5]/div[2]/form/section/section[1]/div/div[1]/div[2]/select").text
print b
browser.execute_script("window.scrollBy(0,200)", "")
a = browser.find_element_by_xpath("html/body/section[5]/div[2]/form/section/section[1]/div/div[5]/div/div/div/div[2]/p").text
print a
