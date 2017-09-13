#-*- coding:utf-8 -*-
import time
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
import unittest
class testLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get("http://yunyingtest.owhat.cn")
        self.browser.maximize_window()
    def test_login(self):
        nowhandle = self.browser.current_window_handle
        # 登录
        self.browser.find_element_by_xpath("html/body/div[1]/div/form/div[2]/div[1]/input").send_keys("13123456789")
        self.browser.find_element_by_xpath("html/body/div[1]/div/form/div[2]/div[2]/input").send_keys("111111")
        time.sleep(1)
        self.browser.find_element_by_xpath("html/body/div[1]/div/form/div[2]/button").click()
        allhandles = self.browser.window_handles
        for handle in allhandles:
            if handle != nowhandle:
                self.browser.switch_to_window(handle)
        time.sleep(1)
        a = self.browser.find_element_by_xpath("html/body/section[5]/div[2]/div[1]/div/ul/li/a/span[1]").text
        self.text = a

        self.assertEqual(self.text,u"O星人xDszMQ","ok")
    def tearDown(self):
        self.browser.quit()

if __name__ =='__main__':
    report_title = u'Example用例执行报告'
    desc = u'用于展示修改样式后的HTMLTestRunner'
    report_file = 'D:\\ExampleReport.html'

    testsuite = unittest.TestSuite()
    testsuite.addTest(testLogin("test_login"))

    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(testsuite)
    #unittest.main()