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
import keyword
# 打开owhat网站
browser = webdriver.Chrome()
browser.get("http://mobile2.owhat.cn")
def denglu(tel,psw):
    #最大化窗口
    browser.maximize_window()
    #登录
    browser.find_element_by_link_text("登录").click()
    time.sleep(1)
    browser.find_element_by_name("account[login]").send_keys(tel)
    browser.find_element_by_name("account[password]").send_keys(psw)
    time.sleep(1)
    browser.find_element_by_xpath("html/body/div[3]/form/p/input").click()
#denglu("13699146624","123456789")
