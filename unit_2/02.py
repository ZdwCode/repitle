import requests;

url="https://fanyi.baidu.com/sug"
kw=input("输入")
data={
    'kw':kw
}
#发送post请求
response=requests.post(url,data=data);
print(response.json())