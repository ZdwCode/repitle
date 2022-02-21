#爬取520电影网海昏侯电视剧
import re
import requests
import asyncio
import aiohttp
import aiofiles

async def downlaod_ts(url,session):
    async with session.get(url) as resp:
        async with aiofiles.open(f'./海昏侯/{url.split("/")[-1]}',mode='wb') as f:
            await f.write(await resp.content.read())

    print('下载完毕')
async def aio_download():
    tasks=[]
    async with aiohttp.ClientSession() as session:#提前准备好session
        async with aiofiles.open("海昏侯第一集_m3u8_第二层.txt",mode='r',encoding='utf-8') as f:
            async for line in f:
                if not line.startswith('#'):
                    line = line.strip();
                    task = asyncio.create_task(downlaod_ts(line, session))
                    tasks.append(task)

            await asyncio.wait(tasks)


def down_m3u8_file(url,title,headers):
    print(url,'here')
    resp=requests.get(url,headers=headers)
    print(resp.text)
    with open(title,mode='w') as f:
       f.write(resp.text)


def main(url):

    # # 获取网页源代码找到m3u8文件
    # resp = requests.get(url)
    # resp.encoding =' utf-8'
    # # 用正则表达式匹配到我们需要的m3u8路径
    # ojb = re.compile(r'''<div class="container">.*?"url":"(?P<url>.*?)",''',re.S)
    # first_m3u8_url = ojb.search(resp.text).group('url')
    # # 去掉反斜杠
    # first_m3u8_url = first_m3u8_url.replace('\\','')
    # print(first_m3u8_url,'处理好之后的第一层')
    # domain=first_m3u8_url.split('/20220220')[0]
    # # 下载第一层的m3u8文件
    # headers={
    #     "User - Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    #     "Host": "new.iskcd.com",
    #     "Origin": "https://www.520ajj.com"
    # }
    # down_m3u8_file(first_m3u8_url,"海昏侯第一集_m3u8.txt",headers=headers)
    # print('第一个m3u8文件已经下载好了') #https://new.iskcd.com/20220220/VHbsUVSn/index.m3u8
    # #domain="https://new.iskcd.com";测试用
    # #下载第二层m3u8文件
    # with open("海昏侯第一集_m3u8.txt",mode='r') as f :
    #     for line in f:
    #         if not line.startswith('#'):
    #             #拼接地址
    #             line=line.strip()
    #             secende_m3u8_url=domain+line;
    #             #print(secende_m3u8_url)
    #             headers={
    #
    #             }
    #             print(secende_m3u8_url)
    #             down_m3u8_file(url=secende_m3u8_url,title='海昏侯第一集_m3u8_第二层.txt',headers=headers);

    #下载视频
    asyncio.run(aio_download())

if __name__ == '__main__':
    url='https://www.520ajj.com/vodplay/haihunhou-1-1.html'
    main(url)