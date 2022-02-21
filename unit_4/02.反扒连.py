
#梨视频主页面的url
import requests
from lxml import etree;
index_url='''https://www.pearvideo.com/'''
resp_index=requests.get(index_url)
resp_index.encoding='utf-8'
# page=etree.HTML(resp_index.text)
# div_video=page.xpath('/html/body/div[2]/div[2]/div/div/div/a/div[1]/div/div[2]');
# print(div_video)#这里爬出来是空的 因为页面在此处使用了js脚本工具 页面源代码中并不会显示

#想获得视频首先得进入子页面
page=etree.HTML(resp_index.text)
child_url=index_url+page.xpath('/html/body/div[2]/div[2]/div/div/div/a/@href')[0]

#得到contid
contid=child_url.split('_')[-1];

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "Referer": child_url
}
videostatus=requests.get(f'https://www.pearvideo.com/videoStatus.jsp?contId={contid}&mrd=0.6680820862592793',headers=headers)
#取出需要的视频地址
dic=videostatus.json()
srcurl=dic['videoInfo']['videos']['srcUrl'];
systemtime=dic['systemTime']
srcurl=srcurl.replace(systemtime,'cont-'+contid)
#https://video.pearvideo.com/mp4/adshort/20220111/cont-1749725-15815507_adpkg-ad_hd.mp4
#开始下载
with open('1.mp4','wb') as f:
    f.write(requests.get(srcurl).content)
