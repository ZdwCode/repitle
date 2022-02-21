
import requests

url='https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=0'
param={
    "sort": "U",
    "range": "0,10",
    "tags": "",
    "start": 0
}
header={
    "User-Agent": "Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 98.0.4758.80 Safari/37.36 Edg/98.0.1108.43"}
response=requests.get(url=url,headers=header);
result=response.json()
print(response.json())
print(len(result))
for item in result:
    print(item)
response.close();