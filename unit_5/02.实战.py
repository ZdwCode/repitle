'''利用线程池爬取北京新发地所有的菜价'''
import requests
import csv;
from concurrent.futures import ThreadPoolExecutor;
f=open('data.csv',mode='w',encoding='utf-8');
CSVwriter=csv.writer(f)

def download_one_page(url,data):
    response=requests.post(url,data=data)
    response.encoding='utf-8'
    current=response.json()
    items = current['list']
    for item in items:
        CSVwriter.writerow(item.values())

    print(data['current']+'页成功爬取')


if __name__ == '__main__':
    url="http://www.xinfadi.com.cn/getPriceData.html"

    with ThreadPoolExecutor(50) as t:
        for i in range(1,200):
            data = {
                'limit': 20,
                'current': f'{i}',
                'pubDateStartTime': '',
                'pubDateEndTime': '',
                'prodPcatid': '',
                'prodCatid': '',
                'prodName': ''
            }
            t.submit(download_one_page,url=url,data=data)


