import requests;

if __name__=="__main__":
    #指定url
    url='https://www.sogou.com/web?query=周杰伦'

    #处理url所携带的参数
    kw=input("enter a word");
    header={"User-Agent": "Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 98.0.4758.80 Safari/37.36 Edg/98.0.1108.43"

    }
    param={
        'query':kw
    }
    response = requests.get(url=url)
    print(response.text)
