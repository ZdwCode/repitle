import asyncio;
import aiohttp

urls=[
    'http://kr.shanghai-jiuxin.com/file/2022/0218/4c4330d02e21d25963a98e0bdbbeeff5.jpg',
    'http://kr.shanghai-jiuxin.com/file/2022/0218/f14087f1fe5f9f1e3a7ab49bb9552a19.jpg',
    'http://kr.shanghai-jiuxin.com/file/2022/0218/36d474deade573fd26dc66affccea101.jpg'
]

async def aiodownload(url):
    #发送请求
    name=url.rsplit('/',1)[1];
    async with aiohttp.ClientSession() as session:  #s相当于requests
        async with session.get(url) as resp:
            #resp.content.read()#等价于response.content
            with open(file=name,mode='wb') as f:
                f.write(await resp.content.read())

    #获得图片
    #保存
async def main():
    tasks=[]
    for url in urls:
        tasks.append(aiodownload(url))#tasks中存放一个个的协程对象

    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())