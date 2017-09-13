#-*- coding:utf-8 -*-
m=list(raw_input("请输入字符串："))
# print(len(m))
i=0
j=1
if len(m) == 0:
    print "请输入字符串，谢谢"
if len(m) == 1:
    print "1" + m[0]
else:
    for i in range(len(m)-1):
        if  m[i] == m[i+1] and i < (len(m)-2):
            j+=1
        elif m[i] == m[i+1] and i == (len(m)-2):
            j += 1
            print str(j)+m[i],
        elif i == (len(m)-2):
            print str(j)+m[i],
            print "1"+m[i+1],
        else:
            print str(j)+m[i],
            i+=1
            j=1



