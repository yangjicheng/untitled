import xlrd
from login import *
excel = xlrd.open_workbook(r'D:\owhattest.xlsx')
from launch import launch
from datetime import datetime
from xlrd import xldate_as_tuple
#print excel.sheet_names()

sheet = excel.sheet_by_name("test")
rows = list(sheet.row_values(1))
print rows
typenumber = str(int (rows[1]))
title = rows[2]
path = str (rows[3])
description = rows[4]
starname = rows[5]
keyword = str(int (rows[6]))
fansclub = rows[7]
st = rows[8]
#print st
stime = datetime(*xldate_as_tuple(st,0))
starttime = stime.strftime('%Y/%d/%m %H:%M:%S')
#print starttime
et = rows[9]
etime = datetime(*xldate_as_tuple(et,0))
endtime = etime.strftime('%Y/%d/%m %H:%M:%S')
provincenumber = str(int (rows[10]))
citynumber = str(int (rows[11]))
price = str(int (rows[12]))
pricetype = str(rows[13])
inventory = str(int (rows[14]))
limit = str(int (rows[15]))
limitnumber = str(int (rows[16]))

launch(typenumber,title,path,description,starname,keyword,fansclub,starttime,endtime,provincenumber,citynumber,price,pricetype,inventory,limit,limitnumber)
time.sleep(3)
browser.find_element_by_xpath("html/body/section[5]/div[2]/section/section/div[2]/div/div[2]/div/div[2]/table/tbody/tr[2]/td[14]/div/a").click()
browser.find_element_by_xpath("html/body/section[5]/div[2]/section/section/div[2]/div/div[2]/div/div[2]/table/tbody/tr[2]/td[14]/div/div/div/a[1]").click()