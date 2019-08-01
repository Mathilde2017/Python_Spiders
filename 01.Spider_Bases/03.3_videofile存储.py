'''
获取到下载文件的 URL，二进制方式下载
urllib request中提供的 urlretrieve() 可进行音视频文件的下载
也支持将远程数据下载到本地

urlretrieve(url, filename=None, reporthook=None, data=None):
filename：数据存储路径+文件
reporthook：要求回调函数。连接上服务器或者响应数据传输下载完毕时触发该函数，
            显示当前的下载进度。
data：(filename,headers)元组
'''

from urllib import request
import requests,os
import random
from lxml import etree

def Schedule(blocknum,blocksize,totalsize):
    '''
    :param blocknum:    已经下载的数据块
    :param blocksize:   数据块的大小
    :param totalsize:   远程文件的大小
    :return:
    '''

    per = 100.0*blocknum*blocksize/totalsize
    if per>100:
        per = 100
    print("当前下载进度为：{}".format(per))
user_agent = [
    "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0",
    "Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"
]

headers = {
    'User_Agent' : random.choice(user_agent)
}

url = "https://www.ivsky.com/tupian/ziranfengguang/"
response = requests.get(url,headers=headers)

html = etree.HTML(response.text)

# 找到所有图片的链接
img_urls = html.xpath('//div[@class="il_img"]//img/@src')
print(img_urls)
# ['//img.ivsky.com/img/tupian/li/201811/25/dahai-008.jpg',

for img_url in img_urls:
    root_dir = 'img'
    if not os.path.exists(root_dir):
        os.mkdir(root_dir)
    filename = img_url.split('/')[-1].split('.')[0]
    img_url = 'https:'+img_url  # 需要构建完整地址
    request.urlretrieve(img_url,root_dir+'/'+filename+'.jpg',Schedule)
    # 注意：Schedule 不要加 ()
