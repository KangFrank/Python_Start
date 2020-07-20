"""
import requests #导入包，requests在网络爬虫中应用非常多

#定义link为目标网页地址
link = "http://www.santostang.com/"
#定义请求头的浏览器代理，把爬虫伪装成浏览器
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0"}
#请求网页
r = requests.get(link,headers=headers)

#输出获取的网页内容代码
print(r.text)
"""
import requests
from bs4 import BeautifulSoup #从bs4这个库中导入BeautifulSoup包，在后边会有关于他的详细教程

#定义link为目标网页地址
link = "http://www.santostang.com/"
#定义请求头的浏览器代理，把爬虫伪装成浏览器
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0"}
#请求网页
r = requests.get(link,headers=headers)

#使用BeautifulSoup解析
soup = BeautifulSoup(r.text,"html.parser")
#找到第一篇文章的标题 h1 ，定位到class是“post-title”的 h1 元素，提取a和a里的字符串，再用strip()去掉空格
title = soup.find("h2",class_="uptop").a.text.strip()

                 
#打印一下看看有没有成功提取标题
print(title)
with open("bug1.txt","a+") as f:
	f.write(title)
