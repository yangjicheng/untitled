#coding:utf-8
import requests
import json
from readExcel import readExcel
class testApi(object):
    def __init__(self,method,url,data):
        self.method = method
        self.url = url
        self.data = data
    @property
    def testApi(self):
        try:
            if self.method == 'post':
                #a = {"apiv":"1.0.0", "client":"{'platform':'ios','deviceid':'67550314-68FC-4CAA-A8A3-29DF9BF259B2','channel':'AppStore','version':'4.2.5'}","cmd_m":"findshoplist",'cmd_s':"shop.goods",'data':"{'pagesize':'20','orderby':['00','00'],'pagenum':'1','columnid':'1'}",'requesttimestap':'1504580605.882372','token':'9eb1add6a74b233b76dac6c1a1c931f1','userid':'15630','v':'1.0'}
                #print type(a)
                global request
                request= requests.post(self.url,data=eval(self.data))
                #print r
               # print r.json()
                #print type(eval(self.data))

            elif self.method == 'get':
                request = requests.get(self.url,params=eval(self.data))
            return request
        except:
            print (u"失败")



    def getStatus(self):
        status = self.testApi.status_code
        return status


    def getJson(self):
        json_data = self.testApi.json()
        return json_data
