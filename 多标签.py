#-*- coding:utf-8 -*-
import time
from selenium import webdriver
import MySQLdb
import win32api
import win32gui
import win32con
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import keyword
#打开owhat网站
browser = webdriver.Chrome()
browser.get("http://mobile2.owhat.cn")
#最大化窗口
browser.maximize_window()
#获取当前窗口
nowhandle=browser.current_window_handle
#登录
browser.find_element_by_link_text("登录").click()
time.sleep(1)
browser.find_element_by_name("account[login]").send_keys("13699146624")
browser.find_element_by_name("account[password]").send_keys("123456789")
time.sleep(1)
browser.find_element_by_xpath("html/body/div[3]/form/p/input").click()
#搜索任务
time.sleep(1)
browser.find_element_by_xpath("html/body/div[1]/div/span[1]/form/div/input").send_keys(u"测试活动")
browser.find_element_by_xpath("html/body/div[1]/div/span[1]/form/div/input").send_keys(Keys.ENTER)
#点击任务
time.sleep(1)
browser.find_element_by_xpath("html/body/div[2]/div[2]/div/div[1]/div/div[1]/a/img").click()
time.sleep(3)
#滚动页面
#browser.execute_script("window.scrollBy(0,200)","")
#获取所有窗口
allhandles=browser.window_handles
#判断窗口是否当前窗口
for handle in allhandles:
   if handle != nowhandle:
       browser.switch_to_window(handle)
#选择品类
browser.find_element_by_xpath("html/body/div[2]/div/div[1]/form/div[1]/div[2]/ul[1]/li[2]").click()
browser.find_element_by_xpath("html/body/div[2]/div/div[1]/form/div[1]/div[2]/ul[2]/li[2]").click()
browser.find_element_by_xpath("html/body/div[2]/div/div[1]/form/div[2]/button[2]").click()
#获取第二个窗口
secondhandle=browser.current_window_handle
#新增地址
time.sleep(2)
browser.find_element_by_xpath("html/body/div[2]/div[2]/a").click()
time.sleep(1)
#获取所有窗口
allhandles=browser.window_handles
#判断窗口是否当前窗口
for handle in allhandles:
    if handle != nowhandle or secondhandle:
        browser.switch_to_window(handle)
time.sleep(1)
#获取第三个窗口
thirdhandle=browser.current_window_handle
#滚动页面
#browser.execute_script("window.scrollBy(0,200)","")
#browser.find_element_by_xpath("html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div[1]/div/a").click()
#time.sleep(1)
#win32api.keybd_event(13, 0, 0, 0)
#win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
#time.sleep(1)
#browser.switch_to_window(thirdhandle)
#增加地址信息
time.sleep(2)
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[1]/input[1]").send_keys(u"姓名")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[2]/input").send_keys("13699146624")
time.sleep(1)
province=browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[3]/div/select[1]")
Select(province).select_by_index(8)
city=browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[3]/div/select[2]")
Select(city).select_by_index(10)
area=browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[3]/div/select[3]")
Select(area).select_by_index(6)
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[4]/input").send_keys(u"杏树屯镇桃园村")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[5]/div/label/input").click()
#新增地址
time.sleep(1)
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[6]/button").click()
time.sleep(1)
browser.close()
browser.switch_to_window(secondhandle)
#滚动页面
time.sleep(1)
browser.execute_script("window.scrollBy(0,300)","")
time.sleep(1)
browser.find_element_by_xpath("html/body/div[2]/form/div[3]/button[1]").click()
time.sleep(1)
browser.find_element_by_xpath("html/body/div[2]/form/div[3]/input[1]").click()
time.sleep(1)
browser.quit()
