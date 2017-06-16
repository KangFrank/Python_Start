"""
#!/usr/bin/python  
# -*- coding: UTF-8 -*-

import urllib.request

def getHtml(url):  
    page = urllib.request.urlopen(url).read()  
    html=page.read()  
    return html  

url="http://baidu.com"  
html=getHtml(url)  
  
print(html)
"""

import re  
import requests  
  
class crawlUser:  
    #定义构造函数  
    def __init__(self, userid,cookie):  
        self.userId = userid  
        self.fellowCount = 0  
        self.fellowlist = []
        self.cookie = cookie  

    def getpage(self):  
        url = "http://www.zhihu.com/people/"+self.userId+"/followers"  
        self.response = requests.get(url, cookies=self.cookie)  
  
    def getfellowcount(self):  
        reg = 'data-tip="p\$t\$(.+)"'  
        pattern = re.compile(reg)  
        self.fellowCount = re.findall(pattern, self.page)  
        count=0  
        for x in self.fellowCount:  
            if (count%2)==0:  
                self.fellowlist.append(x)  
            count=count+1  
        return self.fellowlist  
 
m_cookie={"_za":"****************","a2404_times":"129",  
          "q_c1":"*********************",  
          "_xsrf":"********************",  
          "cap_id":"**************************",  
          "__utmt":"1","z_c0":"***********************1d5358",  
          "unlock_ticket":"***********************6d",  
          "__utma":"********************************",  
          "__utmb":"15**************","__utmc":"*****",  
          "__utmz":"155**********************************/",  
          "__utmv":"***************************************1"}  
  
userlist={}  
tempUserList=["****"]  
flag=0  
iter=0  
while flag<len(tempUserList) and iter<10:  
    user = crawlUser(tempUserList[flag],m_cookie)  
    user.getpage()  
    fellowlist=user.getfellowcount()  
    userlist[tempUserList[flag]]=len(fellowlist)  
    for x in fellowlist:  
        if x not in tempUserList:  
            tempUserList.append(x)  
    print("user %s fellowed %d"%(tempUserList[flag],userlist[tempUserList[flag]]))  
    flag=flag+1  
    iter=iter+1  
  
print("crawl is done!")  
sortRes=sorted(userlist.items(),key=lambda d:d[1])  
"""f=open("userlist.txt","w+") 
58.f.write(userlist) 
59.f.close()"""  
print(sortRes)  
print("sort is done!")

