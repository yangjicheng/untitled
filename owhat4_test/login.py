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
browser.get("http://yunyingtest.owhat.cn")
def login(tel,psw):
    #最大化窗口
    browser.maximize_window()
    #登录
    browser.find_element_by_xpath("html/body/div[1]/div/form/div[2]/div[1]/input").send_keys(tel)
    browser.find_element_by_xpath("html/body/div[1]/div/form/div[2]/div[2]/input").send_keys(psw)
    time.sleep(1)
    browser.find_element_by_xpath("html/body/div[1]/div/form/div[2]/button").click()
# login("13123456789","111111")
