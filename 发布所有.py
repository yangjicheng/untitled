#-*- coding:utf-8 -*-
from login import *
#打开owhat网站
# browser = webdriver.Chrome()
# browser.get("http://mobile2.owhat.cn")
# #最大化窗口
# browser.maximize_window()
# #登录
# browser.find_element_by_link_text("登录").click()
# time.sleep(1)
# browser.find_element_by_name("account[login]").send_keys("13699146624")
# browser.find_element_by_name("account[password]").send_keys("123456789")
# time.sleep(1)
# browser.find_element_by_xpath("html/body/div[3]/form/p/input").click()
# 打开owhat网站
denglu("13699146624","123456789")
time.sleep(1)
#发布任务
browser.find_element_by_xpath("html/body/div[1]/div/span[1]/span/a").click()
browser.find_element_by_xpath("html/body/div[1]/div/span[1]/span/ul/li[3]/a").click()
time.sleep(1)
#发布活动
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/div[2]/div/div[1]/a").click()
time.sleep(1)
#输入活动名称
date = time.strftime('%Y%m%d',time.localtime(time.time()))
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[3]/div/textarea").send_keys(U"回归测试活动"+date)
#描述
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[4]/div/textarea").send_keys(U"描述")
time.sleep(3)
#滚动页面
browser.execute_script("window.scrollBy(0,200)","")
#描述图片
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[5]/div[1]/div/input").send_keys("D:\\123.jpg")
time.sleep(1)
#图片1
browser.execute_script("window.scrollBy(0,200)","")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[6]/div[1]/div").click()
time.sleep(1)
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[6]/div[2]/div[1]").click()
time.sleep(1)
#win32gui上传文件
dialog = win32gui.FindWindow('#32770', u'打开') # 对话框
ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None) # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
button = win32gui.FindWindowEx(dialog, 0, 'Button', None) # 确定按钮Button
win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'D:\\123.jpg') # 往输入框输入绝对地址
win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button) # 按button
#活动时间 购买时间
time.sleep(1)
browser.execute_script("window.scrollBy(0,200)","")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[9]/div/span[1]/input").send_keys("2016-09-10 00:00")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[9]/div/span[2]/input").send_keys("2017-10-18 00:00")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[10]/div/span[1]/input").send_keys("2016-09-10 00:00")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[10]/div/span[2]/input").send_keys("2017-11-10 00:00")
#手机号
time.sleep(1)
browser.execute_script("window.scrollBy(0,200)","")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[12]/div/input").send_keys(random.randint(1, 99999999))
#关联明星
time.sleep(1)
browser.execute_script("window.scrollBy(0,200)","")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[13]/div/span/span[1]/span/ul/li/input").send_keys("a")
time.sleep(1)
browser.find_element_by_xpath("html/body/span/span/span/ul/li[1]").click()
#报名信息
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[14]/a").click()
time.sleep(1)
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[14]/table/tbody/tr/td[1]/div/input").send_keys(u"必填信息")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[14]/table/tbody/tr/td[2]/div/input[2]").click()
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[14]/a").click()
time.sleep(1)
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[14]/table/tbody/tr[2]/td[1]/div/input").send_keys(u"非必填信息")
#价格信息
time.sleep(1)
browser.execute_script("window.scrollBy(0,200)","")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[15]/div/a").click()
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[15]/div/table/tbody/tr/td[1]/div/input").send_keys("11")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[15]/div/table/tbody/tr/td[2]/div/input").send_keys("22")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[15]/div/table/tbody/tr/td[3]/div/input").clear()
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[15]/div/table/tbody/tr/td[3]/div/input").send_keys("0.01")
#预览
time.sleep(1)
browser.execute_script("window.scrollBy(0,200)","")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[19]/input").click()
#发布活动
time.sleep(2)
browser.execute_script("window.scrollBy(0,200)","")
browser.find_element_by_xpath("html/body/div[4]/div/a[2]").click()
time.sleep(2)
#发布任务
browser.find_element_by_xpath("html/body/div[1]/div/span[1]/span/a").click()
browser.find_element_by_xpath("html/body/div[1]/div/span[1]/span/ul/li[3]/a").click()
time.sleep(1)
#发布商品
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/div[2]/div/div[2]/a").click()
time.sleep(1)
#输入商品名称
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[3]/div/textarea").send_keys(U"回归测试商品"+date)
#描述
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[4]/div/textarea").send_keys(U"描述")
time.sleep(3)
#滚动页面
browser.execute_script("window.scrollBy(0,200)","")
#描述图片
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[5]/div[1]/div/input").send_keys("D:\\123.jpg")
time.sleep(1)
#图片1
browser.execute_script("window.scrollBy(0,200)","")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[6]/div[1]/div").click()
time.sleep(1)
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[6]/div[2]/div[1]").click()
time.sleep(1)
#win32gui上传文件
dialog = win32gui.FindWindow('#32770', u'打开') # 对话框
ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None) # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
button = win32gui.FindWindowEx(dialog, 0, 'Button', None) # 确定按钮Button
win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'D:\\123.jpg') # 往输入框输入绝对地址
win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button) # 按button
#活动时间 购买时间
time.sleep(1)
browser.execute_script("window.scrollBy(0,200)","")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[9]/div/span[1]/input").send_keys("2016-09-10 00:00")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[9]/div/span[2]/input").send_keys("2017-10-18 00:00")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[10]/div/span[1]/input").send_keys("2016-09-10 00:00")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[10]/div/span[2]/input").send_keys("2017-11-10 00:00")
#手机号
time.sleep(1)
browser.execute_script("window.scrollBy(0,200)","")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[12]/div/input").send_keys(random.randint(1, 99999999))
#关联明星
time.sleep(1)
browser.execute_script("window.scrollBy(0,200)","")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[13]/div/span/span[1]/span/ul/li/input").send_keys("a")
time.sleep(1)
browser.find_element_by_xpath("html/body/span/span/span/ul/li[1]").click()
#报名信息
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[14]/a").click()
time.sleep(1)
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[14]/table/tbody/tr/td[1]/div/input").send_keys(u"必填信息")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[14]/table/tbody/tr/td[2]/div/input[2]").click()
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[14]/a").click()
time.sleep(1)
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[14]/table/tbody/tr[2]/td[1]/div/input").send_keys(u"非必填信息")
#价格信息
time.sleep(1)
browser.execute_script("window.scrollBy(0,200)","")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[15]/div/a").click()
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[15]/div/table/tbody/tr/td[1]/div/input").send_keys("11")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[15]/div/table/tbody/tr/td[2]/div/input").send_keys("22")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[15]/div/table/tbody/tr/td[3]/div/input").clear()
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[15]/div/table/tbody/tr/td[3]/div/input").send_keys("0.01")
#预览
time.sleep(1)
browser.execute_script("window.scrollBy(0,200)","")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[19]/input").click()
#发布商品
time.sleep(2)
browser.find_element_by_xpath("html/body/div[4]/div/a[2]").click()
time.sleep(2)
#发布任务
browser.find_element_by_xpath("html/body/div[1]/div/span[1]/span/a").click()
browser.find_element_by_xpath("html/body/div[1]/div/span[1]/span/ul/li[3]/a").click()
time.sleep(1)
#发布应援
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/div[2]/div/div[3]/a").click()
time.sleep(1)
#输入应援名称
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[2]/div/textarea").send_keys(U"回归测试应援"+date)
#输入应援目标
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[3]/div/input").send_keys("1")
#描述
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[4]/div/textarea").send_keys(U"描述")
time.sleep(3)
#滚动页面
browser.execute_script("window.scrollBy(0,200)","")
#描述图片
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[5]/div[1]/div/input").send_keys("D:\\123.jpg")
time.sleep(1)
#图片1
browser.execute_script("window.scrollBy(0,200)","")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[6]/div[1]/div").click()
time.sleep(1)
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[6]/div[2]/div[1]").click()
time.sleep(1)
#win32gui上传文件
dialog = win32gui.FindWindow('#32770', u'打开') # 对话框
ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None) # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
button = win32gui.FindWindowEx(dialog, 0, 'Button', None) # 确定按钮Button
win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'D:\\123.jpg') # 往输入框输入绝对地址
win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button) # 按button
#活动时间 购买时间
time.sleep(1)
browser.execute_script("window.scrollBy(0,200)","")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[9]/div/span[1]/input").send_keys("2016-09-10 00:00")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[9]/div/span[2]/input").send_keys("2017-10-18 00:00")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[10]/div/span[1]/input").send_keys("2016-09-10 00:00")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[10]/div/span[2]/input").send_keys("2017-11-10 00:00")
#手机号
time.sleep(1)
browser.execute_script("window.scrollBy(0,200)","")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[12]/div/input").send_keys(random.randint(1, 99999999))
#关联明星
time.sleep(1)
browser.execute_script("window.scrollBy(0,200)","")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[13]/div/span/span[1]/span/ul/li/input").send_keys("a")
time.sleep(1)
browser.find_element_by_xpath("html/body/span/span/span/ul/li[1]").click()
#报名信息
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[14]/a").click()
time.sleep(1)
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[14]/table/tbody/tr/td[1]/div/input").send_keys(u"必填信息")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[14]/table/tbody/tr/td[2]/div/input[2]").click()
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[14]/a").click()
time.sleep(1)
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[14]/table/tbody/tr[2]/td[1]/div/input").send_keys(u"非必填信息")
#价格信息
time.sleep(1)
browser.execute_script("window.scrollBy(0,200)","")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[15]/div/a").click()
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[15]/div/table/tbody/tr/td[1]/div/input").send_keys("11")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[15]/div/table/tbody/tr/td[2]/div/input").send_keys("22")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[15]/div/table/tbody/tr/td[3]/div/input").clear()
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[15]/div/table/tbody/tr/td[3]/div/input").send_keys("0.01")
#预览
time.sleep(1)
browser.execute_script("window.scrollBy(0,200)","")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[19]/input").click()
#发布应援
time.sleep(2)
browser.find_element_by_xpath("html/body/div[4]/div/a[2]").click()
time.sleep(2)
#发布任务
browser.find_element_by_xpath("html/body/div[1]/div/span[1]/span/a").click()
browser.find_element_by_xpath("html/body/div[1]/div/span[1]/span/ul/li[3]/a").click()
time.sleep(1)
#发布话题
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/div[2]/div/div[4]/a").click()
time.sleep(1)
#输入话题名称
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[1]/div/textarea").send_keys(U"回归测试话题"+date)
#输入描述
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[2]/div/textarea").send_keys(U"描述")
time.sleep(3)
#图片1
browser.execute_script("window.scrollBy(0,200)","")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[3]/div[1]/div").click()
time.sleep(1)
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[3]/div[2]/div[1]").click()
time.sleep(1)
#win32gui上传文件
dialog = win32gui.FindWindow('#32770', u'打开') # 对话框
ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None) # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
button = win32gui.FindWindowEx(dialog, 0, 'Button', None) # 确定按钮Button
win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'D:\\123.jpg') # 往输入框输入绝对地址
win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button) # 按button
#关联明星
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[4]/div/span/span[1]/span/ul/li/input").send_keys("a")
time.sleep(1)
browser.find_element_by_xpath("html/body/span/span/span/ul/li[1]").click()
#预览
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[6]/input").click()
#发布话题
time.sleep(2)
browser.find_element_by_xpath("html/body/div[3]/div/a[2]").click()
time.sleep(2)
#发布任务
browser.find_element_by_xpath("html/body/div[1]/div/span[1]/span/a").click()
browser.find_element_by_xpath("html/body/div[1]/div/span[1]/span/ul/li[3]/a").click()
time.sleep(1)
#发布直播
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/div[2]/div/div[5]/a").click()
time.sleep(1)
#输入直播标题
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[3]/div/textarea").send_keys(U"回归测试直播"+date)
#输入描述
browser.find_element_by_class_name("").send_keys(U"描述")
time.sleep(3)
#图片1
browser.execute_script("window.scrollBy(0,200)","")
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[7]/div[1]/div").click()
time.sleep(1)
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[7]/div[2]/div[1]").click()
time.sleep(1)
#win32gui上传文件
dialog = win32gui.FindWindow('#32770', u'打开') # 对话框
ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None) # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
button = win32gui.FindWindowEx(dialog, 0, 'Button', None) # 确定按钮Button
win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'D:\\123.jpg') # 往输入框输入绝对地址
win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button) # 按button
#关联明星
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[8]/div/span/span[1]/span/ul/li/input").send_keys("a")
time.sleep(1)
browser.find_element_by_xpath("html/body/span/span/span/ul/li[1]").click()
#预览
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/form/div[10]/input").click()
#发布话题
time.sleep(2)
browser.find_element_by_xpath("html/body/div[3]/div/a[2]").click()
time.sleep(2)
