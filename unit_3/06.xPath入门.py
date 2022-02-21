from lxml import etree
import requests
url='''https://jiujiang.zbj.com/search/f/?kw=python'''
resp=requests.get(url)
resp.encoding='utf-8'

#解析
index=1;
html=etree.HTML(resp.text)
goods_divs=html.xpath('/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div')
for good_div in goods_divs:
    adress=good_div.xpath('./div/div/a[1]/div[1]/div/span/text()')[0]
    price=good_div.xpath('./div/div/a[2]/div[2]/div[1]/span[1]/text()')[0].strip('¥')
    amount = good_div.xpath('./div/div/a[2]/div[2]/div[1]/span[2]/text()')[0]
    title_list=good_div.xpath('./div/div/a[2]/div[2]/div[2]/p/text()')
    if len(title_list) !=1:
        title = 'python'.join(title_list)
    else:
        title='python'+title_list[0]
    try:
        print(title)
        print(price,amount,adress)
        print(index)
        
    except Exception as e:
        print(e)
    index+=1;