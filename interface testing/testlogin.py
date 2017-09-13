#coding:utf-8
import unittest
from testApi import testApi
from readExcel import readExcel
import MySQLdb
import json
class testlogin(unittest.TestCase):
    def testlogin(self):
        excel = readExcel(r'D:\testlogin.xlsx')
        name = excel.getName
        data = excel.getData
        url = excel.getUrl
        method = excel.getMethod
        code = excel.getCode
        #row = excel.getRows
        i = 0
        conn = MySQLdb.connect(host="rm-bp1z2lr262rp0ync4o.mysql.rds.aliyuncs.com",user="owhat4transplant",passwd="reS0ygecvq9c",db="owhat4_transplant",port=3306)
        cur = conn.cursor()
        a = cur.execute("SELECT city_name FROM area_city WHERE id = 2")
        print a
        api = testApi(method[i], url[i], data[i])
        apicode = api.getStatus()
        apijson = api.getJson()
        if apicode == code[i]:
            print ('{}、{}:测试成功。json数据为:{}'.format(i + 1, name[i], apijson))
            self.assertEqual(apijson["message"], u"操作成功")
            self.assertEqual(apijson["result"], "success")
        else:
            print ('{}、{}:测试失败'.format(i + 1, name[i]))

        i = 1
        api = testApi(method[i], url[i], data[i])
        apicode = api.getStatus()
        apijson = api.getJson()
        if apicode == code[i]:
            print ('{}、{}:测试成功。json数据为:{}'.format(i + 1, name[i], apijson))
            self.assertEqual(apijson["message"], u"用户名或密码错误")
            self.assertEqual(apijson["result"], "fail")
        else:
            print ('{}、{}:测试失败'.format(i + 1, name[i]))

if __name__ == "__main__":
    unittest.main()