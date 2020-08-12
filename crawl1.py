#!/usr/local/bin/python
#-*-coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import time
import argparse

def get_headers(page, cookie):
    headers = {
        'authority': 'shanghai.anjuke.com',
        'method': 'GET',
        'path': '/community/p{}/'.format(page),
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'cookie': cookie,
        'pragma': 'no-cache',
        'referer': 'https://shanghai.anjuke.com/community/p1/',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
    }
    return headers

def get_html_by_page(page, cookie):
    headers = get_headers(page, cookie)
    url = 'https://shanghai.anjuke.com/community/p{}/'.format(page)
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        print('页面不存在！')
        return None
    return res.text

def extract_data_from_html(html):
    soup = BeautifulSoup(html)
    list_content = soup.find(id="list-content")
    if not list_content:
        return None
    items = list_content.find_all('div', class_='li-itemmod')
    if len(items) == 0:
        return None
    return [extract_data(item) for item in items]

def extract_data(item):
    name = item.find_all('a')[1].text.strip()
    address = item.address.text.strip()
    if item.strong is not None:
        price = item.strong.text.strip()
    else:
        price = None
    finish_date = item.p.text.strip().split('：')[1]
    latitude, longitude = [d.split('=')[1] for d in item.find_all('a')[3].attrs['href'].split('#')[1].split('&')[:2]]
    return name, address, price, finish_date, latitude, longitude

def crawl_all_page(cookie):
    page = 1
    data_raw = []
    while True:
        try:
            html = get_html_by_page(page, cookie)
            data_page = extract_data_from_html(html)
            if not data_page:
                break
            data_raw += data_page
            print('crawling {}th page ...'.format(page))
            page += 1
        except:
            print('maybe cookie expired!')
            break
    print('crawl {} pages in total.'.format(page-1))
    return data_raw

def create_df(data):
    columns = ['name', 'address', 'price', 'finish_date', 'latitude', 'longitude']
    return pd.DataFrame(data, columns=columns)

def clean_data(df):
    df.dropna(subset=['price'], inplace=True)
    df = df.astype({'price': 'float64', 'latitude': 'float64', 'longitude': 'float64'})
    return df

def visual(df):
    fig, ax = plt.subplots()
    df.plot(y='price', ax=ax, bins=20, kind='hist', label='房价频率直方图', legend=False)
    ax.set_title('房价分布直方图')
    ax.set_xlabel('房价')
    ax.set_ylabel('频率')
    plt.grid()
    plt.show()

def run(cookie):
    data = crawl_all_page(cookie)
    df = create_df(data)
    df = clean_data(df)
    visual(df)
    df.sort_values('price', inplace=True)
    df.reset_index(drop=True, inplace=True)
    #  保存 csv 文件
    filename = time.strftime("%Y-%m-%d", time.localtime())
    csv_file = filename + '.csv'
    df.to_csv('anjuke_shanghai_house_price.csv', index=False)

def get_cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--cookie', type=str, help='cookie.')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = get_cli_args()
    run(args.cookie)
#python crawl.py --cookie "sessid=F47286B0-CAEA-F441-E6D1-6B757D714677"