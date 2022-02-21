
'''
requests 模块:模拟浏览器发请求
    使用方法:
    -指定url
    -发起请求
    -获取响应数据
    -持久化存储
'''

import requests

if __name__=="__main__":
    #指定url
    url="https://www.sogou.com/";
    #发起请求
    response=requests.get(url=url)
    #获取响应数据 字符串类型
    page_text=response.text
    print(page_text);
    #持久化存储
    with open('./sogou.html','w',encoding='utf-8') as f:
        f.write(page_text);
    print("爬取数据结束");

