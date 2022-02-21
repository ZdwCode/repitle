'''爬取电影天堂的电影下载连接'''
import requests;
import re;
import csv;
url='''https://m.dytt8.net/'''
domian=url+'index2.htm'
respose=requests.get(domian);
respose.encoding='gb2312'
page_text=respose.text;

obj1=re.compile(r'2022新片精品.*?<ul>(?P<movies>.*?)</ul>',re.S);
obj2=re.compile(r"最新电影下载.*?<a href='(?P<childurl>.*?)'>(?P<name>.*?)</a>",re.S)
obj3=re.compile(r'<a target=".*?" href="(?P<magnet>.*?)">',re.S)
result_1=obj1.finditer(page_text)

f=open('movie_data.csv',mode='w');
CSVwriter=csv.writer(f);

for item in result_1:
    content=item.group('movies')
    #print(content)
    #print('-------------------------------------')
    result_2=obj2.finditer(content);
    for c_item in result_2:
        childurl=c_item.group('childurl');
        name = c_item.group('name')
        #进入子页面 拼接地址
        childurl=url+childurl;
        response_childpage=requests.get(childurl)
        response_childpage.encoding='gbk'
        childpage_text=response_childpage.text;
        #print(childpage_text)
        result_3=obj3.search(childpage_text)
        data={
            'name':name,
            'magnet':result_3.group('magnet')
        }
        CSVwriter.writerow(data.values())
respose.close();
response_childpage.close();

