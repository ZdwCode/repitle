import requests
from bs4 import BeautifulSoup
url='''http://www.xinfadi.com.cn/priceDetail.html'''
response=requests.get(url)
response.encoding='UTF-8'
page_text=response.text;
#解析数据
#1.把页面源代码交给BeautifulSoup进行处理

page=BeautifulSoup(page_text,"html.parser")#指定html解析器
#2.从bs中查找数据 find(标签名，属性)：找到第一个  findall：找到所有匹配的
tbody=page.find("tbody",attrs={
    "id":"tableBody",
    "class":"ul"
})
print(tbody)


