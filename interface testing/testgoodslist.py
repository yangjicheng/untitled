#coding:utf-8
import unittest
import csv
from testApi import testApi
from readExcel import readExcel
from HTMLTestRunner import HTMLTestRunner


class testgoodslist(unittest.TestCase):
    def testgoodslist(self):
        excel = readExcel(r'D:\posttest.xlsx')
        name = excel.getName
        data = excel.getData
        url = excel.getUrl
        method = excel.getMethod
        code = excel.getCode
        row =excel.getRows
        i = 0
        api = testApi(method[i],url[i],data[i])
        apicode = api.getStatus()
        apijson =api.getJson ()
        if apicode == code[i]:
            print ('{}、{}:测试成功。json数据为:{}'.format(i + 1, name[i], apijson))
            self.assertEqual(apijson["message"],u"操作成功")
            self.assertEqual(apijson["result"],"success")
        else :
            print ('{}、{}:测试失败'.format(i + 1, name[i]))
        i = 1
        api = testApi(method[i], url[i], data[i])
        apicode = api.getStatus()
        apijson = api.getJson()
        if apicode == code[i]:
            print ('{}、{}:测试成功。json数据为:{}'.format(i + 1, name[i], apijson))
            self.assertEqual(apijson["message"], u"操作成功")
            self.assertEqual(apijson["result"], "success")
        else:
            print ('{}、{}:测试失败'.format(i + 1, name[i]))
        i = 2
        api = testApi(method[i], url[i], data[i])
        apicode = api.getStatus()
        apijson = api.getJson()
        if apijson["message"] == "success":
            print ('{}、{}:测试成功。json数据为:{}'.format(i + 1, name[i], apijson))
            #self.assertEqual(apijson["message"], u"找不到方法")
            #self.assertEqual(apijson["result"], "fail")
        else:
            print ('{}、{}:测试失败'.format(i + 1, name[i]))

if __name__ == "__main__":
    unittest.main()

