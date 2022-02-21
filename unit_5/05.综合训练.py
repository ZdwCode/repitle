'''
流程：
    1.先拿到主页面的源代码
    2.从源代码中提取到m3u8的url
    3.下载m3u8文件
    4，读取文件 下载视频
    5.合并视频
'''

# import requests
# import re;
# url='https://www.91kanju2.com/vod-play/61412-1-1.html';
# resp=requests.get(url);
# page=resp.text;
# obj=re.compile(r"url: '(?P<url>.*?)',",re.S)
# m3u8_url=obj.search(page).group('url')
# resp.close();
# # 下载m3u8文件
# resp2=requests.get(m3u8_url)
#
# with open('开端.m3u8',mode='wb') as f :
#     f.write(resp2.content)
#
# resp2.close();

#解析m3u8文件
import requests
n=1;

with open('开端.m3u8',mode='r',encoding='utf-8') as f :
    for line in f:
        line = line.strip();#去掉空格换行啥子的
        if line.startswith('#'):# ’#‘开头的不要
            continue;
        #print(line)

        #下载视频的片段
        resp3=requests.get(line)
        f=open(f"./开端/{n}.ts",mode='wb')
        f.write(resp3.content);
        n+=1;
        f.close()
        resp3.close();
 