#拿到页面源代码
#通过re来获取信息

import re;
import requests;
import pymysql
import csv;
info={
    'host':'localhost',
    'port':3306,
    'user':'root',
    'password':'758258'
}
def getconnection():
    con=pymysql.connect(**info);
    cursor=con.cursor();
    sql_show_databases="show databases";
    cursor.execute(sql_show_databases);
    results=cursor.fetchall();
    flag=True
    for item in results:
        if 'douban' ==item[0]:
            flag=False;
    if flag:
        sql_create_douban='''create database douban charset="utf8";'''
        cursor.execute(sql_create_douban);
    sql_use_douban='''use douban;'''
    sql_create_table='''create table movies(
                        id int not null auto_increment primary key,
                        name varchar(20),
                        rate int,
                        comment_nums int
                        );'''
    cursor.execute(sql_use_douban);
    #cursor.execute(sql_create_table);

    return con;
def insert(name,rate,comment):
    con=getconnection();
    cursor=con.cursor();
    sql_use_douban = '''use douban;'''
    cursor.execute(sql_use_douban);
    sql_insert='''insert into movies(name,rate,comment_nums) values(%s,%s,%s);'''
    cursor.execute(sql_insert,[name,rate,int(comment)]);
    cursor.close()
    con.close();

url="https://movie.douban.com/chart";
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43"
}
response=requests.get(url,headers=header);
page_content=response.text;
#解析数据
obj=re.compile(r'<table width="100%" class="">.*?<a class="nbg" href=".*?"  title="(?P<name>.*?)">.*?<span class="rating_nums">(?P<rate>.*?)</span>.*?<span class="pl">(?P<comment>.*?)</span>',re.S);
#obj=re.compile(r'<table width="100%" class="">.*?<a href=".*?"  class="">(?P<name>.*?)/',re.S);
results=obj.finditer(page_content);
f=open('data.csv',mode="w");
CSVwriter = csv.writer(f)
for item in results:
    print('name:'+item.group("name"),'rate:'+item.group("rate"),'comment:'+item.group("comment")[1:-1])
    dic=item.groupdict();
    CSVwriter.writerow(dic.values())
    name=item.group("name");
    print(type(name))
    #insert(name,item.group("rate"),item.group("comment")[1:-4])
f.close();
response.close();




