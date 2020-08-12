# 爬取糗事百科短视频

# Replace the browser to send request and receive response
# Install the third-party module called requests, using "pip install requests --user"

import requests
import re
import os
import time

# start = time.time()

# Download videos

# Set Download Location
save_path = 'D:/pythonlearn/video/q'
if not os.path.exists(save_path):
    os.mkdir(save_path)

count = 0
page = 3
for i in range(1, page+1):
    print('===================正在取第{}页数据================='.format(i))
    url = 'https://www.qiushibaike.com/video/page/{}/' .format(i)
    # print(url)
    # Why we need to write headers? Web crawling is a method to pretend it act as a web browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)  # resp is the response result
    # print(resp) # response code, 200 means successful access, 418 means an anti-web-crawling reject access
    print(resp.request.headers)
    # print(resp.text)
    html_data = resp.text
    # RegEx  Findall(pattern, string) returns list
    # r'' is to tell compiler this is a raw string
    regex = re.compile(r'<source src="(.*?)" type=\'video/mp4\' />')
    info = regex.findall(html_data)
    # info = re.findall(r'<source src="(.*?)" type=\'video/mp4\' />', resp.text)
    print(info)
    # print(type(info))

    lst = []  # save the concatenatd url
    for item in info:
        lst.append('https:' + item)
    # print(lst)


    for item in lst:
        count += 1
        file = '{}/{}.mp4' .format(save_path, count)
        if os.path.exists(file):
            continue
        # send request
        resp = requests.get(item, headers=headers)
        # save each video to the local path
        with open(file, 'wb') as f:
            f.write(resp.content)
            # print each video downloaded progress
            print('成功抓取第{}个视频' .format(count))

print("下载完成")

# end = time.time()
# print("总共耗时：", round(end-start,2), "秒")
