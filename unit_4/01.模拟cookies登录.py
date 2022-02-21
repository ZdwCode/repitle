#登录 ->得到cookie
#带着cookie 请求书架url 得到书架的内容

#会话
import requests
import csv
session=requests.session();
login_url='''https://passport.17k.com/ck/user/login'''
#1.登录
date={
    'loginName':'18179219692',
    'password':'tiancai123'
}
resp_login=session.post(login_url,data=date)
shell_url='''https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919'''
#使用带有cookies的session请求shell_url
resp_shell=session.get(shell_url);
f=open('data_book','w')
CSVwriter =csv.writer(f);
list_data=resp_shell.json()['data']
book_store={}
for book in list_data:
    print(book);
    book_store['bookId']=book['bookId'];
    book_store['bookName']=book['bookName'];
    book_store['authorPenName']=book['authorPenName']
    CSVwriter.writerow(book_store.values())

f.close()