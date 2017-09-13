import MySQLdb
conn=MySQLdb.connect(host="123.57.147.171",user="zhangjidong",passwd="WiDMU9UMtrYkExBgy6wn",db="owhat3_staging2",port=29854)
cur = conn.cursor()
a=cur.execute("SELECT updated_at,code FROM `core_mobile_codes` WHERE `mobile` LIKE '%13810273089%' ORDER BY updated_at desc LIMIT 1")

print(a)