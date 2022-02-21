import os
from bs4 import BeautifulSoup;
import requests
import time
print('hello python')
url='''https://www.keaitupian.cn/'''
response=requests.get(url);
response.encoding='utf-8'
page=BeautifulSoup(response.text,'html.parser');
# topText_div=page.find('div',class_='toptip')
# print(topText_div.text)
attrs={
    'class':'related_img',
    'style':'display:inline'
}
ul=page.find('ul',attrs=attrs)

li_list=ul.findAll('li',class_='related_boxindex')

for li in li_list:
    a=li.find('a')
    href=a.get('href')
    title=a.get('title')
    if not os.path.exists(title):
        os.makedirs(title)
    print(title+':已经创建好了')
    #print(url+href)
    child_resp=requests.get(url+href)
    child_page_text=child_resp.text;
    child_page=BeautifulSoup(child_page_text,'html.parser')
    article=child_page.find('article',class_='article-content')

    img_list=article.findAll('p',style='text-align:center;',class_='')
    for img in img_list:
        img_src=img.find('img')
        img_url=img_src.get('src')
        #获取图片路径
        filename=title+'/'+img_url.split('/')[-1]
        print(filename)
        with open(filename,mode='wb') as f:
            image_resp=requests.get(img_url)
            f.write(image_resp.content)
            image_resp.close();

    time.sleep(5)