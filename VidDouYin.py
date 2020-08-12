# 爬取抖音短视频

# python 3.6 - 3.8
# pycharm
# requests
# re

'''
爬虫的一般思路

1、分析目标网页，确定爬取的url路径，headers参数

2、发送请求 -- requests 模拟浏览器发送请求，获取响应数据

3、解析数据 -- 正则表达式

4、保存数据 -- 保存在目标文件夹中
'''

# 导入工具
import requests
import re
import os


# 保存数据 -- 保存在目标文件夹中
save_path = 'C:/Users/win10/Desktop'
if not os.path.exists(save_path):
    os.mkdir(save_path)    
    
# 分析目标网页，确定爬取的url路径，headers参数
# base_url = 'http://douyin.bm8.com.cn/d_1.html'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
# }

count = 0
# 构建一个for循环
for page in range(8, 10):
    print('===================正在取第{}页数据================='.format(page))
    # 1、分析目标网页，确定爬取的url路径，headers参数
    base_url = 'http://douyin.bm8.com.cn/d_{}.html'.format(page)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    # 发送请求 -- requests 模拟浏览器发送请求，获取响应数据
    resp = requests.get(url=base_url, headers=headers)
    html_data = resp.text
    # 解析数据 -- 正则表达式
    pattern = re.compile(r'onclick="open1\(\'(.*?)\',\'(.*?)\',\'\'\)"')
    result = pattern.findall(html_data)
    print(result)
    
    # 处理文件名非法字符
    def change_title(title):
        pattern = re.compile(r"[\/\\\:\*\?\"\<\>\|]")  # '/ \ : * ? " < > |'
        new_title = re.sub(pattern, "_", title)  # 替换为下划线
        return new_title


    for title, url in result:
        count += 1
        # 处理文件名非法字符
        new_title = change_title(title)
        # 建立路径+文件名
        file = '{}/{}_{}.mp4'.format(save_path, count, new_title)
        if os.path.exists(file):
            continue
        # 请求抖音视频数据
        data = requests.get(url=url, headers=headers).content
        with open(file, mode='wb') as f:
            f.write(data)
            print('成功抓取第{}个视频' .format(count))
    
print("下载完成")

# end = time.time()
# print("总共耗时：", round(end-start,2), "秒")
