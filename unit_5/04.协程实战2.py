'''爬取一部小说'''
import asyncio
import json
import aiohttp
import requests
import aiofiles
#4306063500
#http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"} ==response里面包含了章节的cid和title
#http://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|1569782244","need_bookinfo":1}

async def aio_download(book_id,c_id,title):
    #先拼接一个url出来
    data = {
        "book_id": book_id,
        "cid": f"{book_id}|{c_id}",
        "need_bookinfo": 1
    }
    data=json.dumps(data)
    url='''http://dushu.baidu.com/api/pc/getChapterContent?data='''+data;

    #得到url之后开始异步请求
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic=await resp.json();
            content=dic['data']['novel']['content'];
            filename="./西游记/"+title
            async with aiofiles.open(filename,mode='w',encoding='utf-8') as f:
                await f.write(content)




def cat_download(url,book_id):
    #得到小说的章节信息
    resp=requests.get(url)
    dic=resp.json()
    items=dic['data']['novel']['items']
    tasks=[]
    for item in items:
        title=item['title'];
        c_id=item['cid']

        #准备异步的任务
        tasks.append(aio_download(book_id,c_id,title))

    asyncio.run(asyncio.wait(tasks))




if __name__ == '__main__':
    #book_id=input('请输入小说的id')
    book_id='4306063500';
    url='''http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"'''+book_id+'''"}'''
    cat_download(url,book_id)