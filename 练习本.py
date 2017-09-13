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
from login import *
denglu("13699146624","123456789")
time.sleep(1)
#发布任务
browser.find_element_by_xpath("html/body/div[1]/div/span[1]/span/a").click()
browser.find_element_by_xpath("html/body/div[1]/div/span[1]/span/ul/li[3]/a").click()
time.sleep(1)
#发布直播
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/div[2]/div/div[5]/a").click()
time.sleep(3)
#输入描述
browser.switch_to_frame("frame_reference")
browser.find_element_by_class_name("ke-content").send_keys(U"描述")