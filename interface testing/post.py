#coding:utf-8
import requests
import unittest
class Test_post(unittest.TestCase):
    def setUp(self):
        pass
    def test_post(self):
       self.data={
             "apiv":"1.0.0",
            "client":"{'platform':'ios','deviceid':'67550314-68FC-4CAA-A8A3-29DF9BF259B2','channel':'AppStore','version':'4.2.5'}",
            "cmd_m":"findshoplist",
            'cmd_s':"shop.goods",
            'data':"{'pagesize':'20','orderby':['00','00'],'pagenum':'1','columnid':'1'}",
            'requesttimestap':'1504580605.882372',
            'token':'9eb1add6a74b233b76dac6c1a1c931f1',
            'userid':'15630',
            'v':'1.0'
       }
       r = requests.post(url="http://appo4test.owhat.cn/api",data=self.data)

       json =  r.json()
       print json["message"]
       print json
       self.assertEqual(r.status_code,200)
       self.assertEqual(json['message'],U"操作成功")

if __name__ == "__main__":
    unittest.main()