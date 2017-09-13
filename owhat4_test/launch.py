#-*- coding:utf-8 -*-
from login import *
from selenium.webdriver.support.select import Select
#发布任务
def launch(typenumber,title,path,description,starname,keyword,fansclub,starttime,endtime,provincenumber,citynumber,price,pricetype,inventory,limit,limitnumber):
    login("13123456789", "111111")
    time.sleep(1)
    nowhandle = browser.current_window_handle
    time.sleep(1)
    browser.find_element_by_xpath("html/body/section[5]/div[1]/div[2]/ul/li[1]/a/span").click()
    time.sleep(1)
    browser.find_element_by_xpath("html/body/section[5]/div[1]/div[2]/ul/li[1]/ul[1]/li/a").click()
    time.sleep(1)
    browser.find_element_by_xpath("html/body/section[5]/div[2]/section/section/header/a").click()

    time.sleep(1)
    # 获取所有窗口
    allhandles = browser.window_handles
    # 判断窗口是否当前窗口
    for handle in allhandles:
        if handle != nowhandle:
            browser.switch_to_window(handle)
    #官方或者饭制
    Select(browser.find_element_by_xpath("html/body/section[5]/div[2]/form/section/section[1]/div/div[1]/div[2]/select")).select_by_value(typenumber)    #  4   官方   5   饭制
    #标题
    browser.find_element_by_xpath("html/body/section[5]/div[2]/form/section/section[1]/div/div[3]/div/input").send_keys(title)
    #上传图片
    browser.find_element_by_xpath("html/body/section[5]/div[2]/form/section/section[1]/div/div[4]/div/div[1]/input").click()
    time.sleep(1)
    dialog = win32gui.FindWindow('#32770', u'打开')  # 对话框
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
    Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
    button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
    win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, path)  # 往输入框输入绝对地址
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
    time.sleep(1)
    browser.find_element_by_xpath("html/body/div[3]/div/div/div[3]/button").click()
    #描述
    browser.find_element_by_xpath("html/body/section[5]/div[2]/form/section/section[1]/div/div[5]/div/div/div/div[2]").send_keys(description)
    #滚动页面
    browser.execute_script("window.scrollBy(0,200)", "")
    #关联明星
    browser.find_element_by_xpath("html/body/section[5]/div[2]/form/section/section[1]/div/div[6]/div/div/input").send_keys(starname)
    time.sleep(1)
    browser.find_element_by_xpath("html/body/section[5]/div[2]/form/section/section[1]/div/div[6]/div/div/ul/li/a").click()
    #关键词
    browser.find_element_by_xpath("html/body/section[5]/div[2]/form/section/section[1]/div/div[8]/div/div/input").send_keys(keyword)
    #粉丝会机构
    browser.find_element_by_xpath("html/body/section[5]/div[2]/form/section/section[1]/div/div[9]/div/div/input").send_keys(fansclub)
    time.sleep(1)
    browser.find_element_by_xpath("html/body/section[5]/div[2]/form/section/section[1]/div/div[9]/div/div/ul/li/a").click()
    # 滚动页面
    browser.execute_script("window.scrollBy(0,200)", "")
    #附加信息
    browser.find_element_by_xpath("html/body/section[5]/div[2]/form/section/section[2]/div/div[1]/div/label[1]/input").click()
    browser.find_element_by_xpath("html/body/section[5]/div[2]/form/section/section[2]/div/div[1]/div/label[5]/input").click()
    #browser.find_element_by_xpath("html/body/section[5]/div[2]/form/section/section[2]/div/div[2]/div/div[2]/div/button").click()
    #browser.find_element_by_xpath("html/body/section[5]/div[2]/form/section/section[2]/div/div[2]/div/div[3]/table/tbody/tr[4]/td[1]/input").click()
    # 滚动页面
    browser.execute_script("window.scrollBy(0,200)", "")
    #售卖时间
    browser.find_element_by_xpath("html/body/section[5]/div[2]/form/section/section[2]/div/div[3]/div[1]/em/input").send_keys(starttime)
    browser.find_element_by_xpath("html/body/section[5]/div[2]/form/section/section[2]/div/div[3]/div[2]/em/input").send_keys(endtime)
    # 滚动页面
    browser.execute_script("window.scrollBy(0,200)", "")
    #发货城市
    Select(browser.find_element_by_xpath("html/body/section[5]/div[2]/form/section/section[2]/div/div[5]/div[1]/select")).select_by_value(provincenumber)
    time.sleep(1)
    Select(browser.find_element_by_xpath("html/body/section[5]/div[2]/form/section/section[2]/div/div[5]/div[2]/select")).select_by_value(citynumber)
    #取消包邮
    browser.find_element_by_xpath("html/body/section[5]/div[2]/form/section/section[2]/div/div[7]/div[1]/div/input[1]").click()
    # 滚动页面
    browser.execute_script("window.scrollBy(0,200)", "")
    #标签
    browser.find_element_by_xpath("html/body/section[5]/div[2]/form/section/section[2]/div/div[9]/div/input[1]").click()
    # 滚动页面
    browser.execute_script("window.scrollBy(0,200)", "")
    #新增品类
    browser.find_element_by_xpath("html/body/section[5]/div[2]/form/section/section[3]/div[1]/div[4]/div/div[1]/button").click()
    time.sleep(1)
    browser.find_element_by_xpath("html/body/div[2]/div/div/div/div[2]/form/div[2]/div/input").send_keys(price)
    browser.find_element_by_xpath("html/body/div[2]/div/div/div/div[2]/form/div[3]/div/input").send_keys(pricetype)
    browser.find_element_by_xpath("html/body/div[2]/div/div/div/div[2]/form/div[4]/div[1]/input").send_keys(inventory)
    if limit == 0 :
        browser.find_element_by_xpath("html/body/div[2]/div/div/div/div[2]/form/div[5]/div/input[2]").click()
    else :
        browser.find_element_by_xpath("html/body/div[2]/div/div/div/div[2]/form/div[6]/div/input").send_keys(limitnumber)
    time.sleep(1)
    browser.find_element_by_xpath("html/body/div[2]/div/div/div/div[3]/button[2]").click()
    time.sleep(1)
    browser.find_element_by_xpath("html/body/section[5]/div[2]/form/section/div/div/button[1]").click()


