#-*- coding:utf-8 -*-

from login import *
import time
denglu("13699146624","123456789")
time.sleep(1)
# 发布任务
browser.find_element_by_xpath("html/body/div[1]/div/span[1]/span/a").click()
browser.find_element_by_xpath("html/body/div[1]/div/span[1]/span/ul/li[3]/a").click()
time.sleep(1)
#发布活动
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/div[2]/div/div[1]/a").click()
time.sleep(1)
#  发布活动，什么都不填点预览
browser.execute_script("window.scrollBy(0,200)","")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[19]/input").click()
#print(browser.current_url)
if browser.current_url =="http://mobile2.owhat.cn/shop/events/new" :
    print("launch 1 event    success")
else:
    print("launch 1 event    failed")
browser.back()
time.sleep(1)
#发布活动
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/div[2]/div/div[1]/a").click()
time.sleep(1)
#输入活动名称
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[3]/div/textarea").send_keys(U"自动发布测试活动自动发布测试活动自动发布测试活动自动发布测试活动自动发布测试活动自动发布测试活动")
#描述
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[4]/div/textarea").send_keys(U"描述")
