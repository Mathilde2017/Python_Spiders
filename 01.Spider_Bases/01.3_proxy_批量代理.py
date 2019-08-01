'''
原因：
    在现实爬虫中，使用代理IP，是爬虫的常用手段
    代理用来隐藏真实访问中，代理也不允许频繁访问某一个固定网站，所以，代理一定要很多很多
目标：
    1.构建代理集群/队列
    2.每次访问服务器，随机抽取一个代理。抽取可以使用 random.choice
分析：
    1.构建用户代理群
    2.每次访问，随机选取代理并执行
步骤：
    1.设置代理地址
    2.创建ProxyHandler    proxy_handler = request.ProxyHandler(proxy)
    3.创建Opener          opener = request.build_opener(proxy_handler)
    4.安装Opener          request.install_opener(opener)
    5.request请求         rsp = request.urlopen(url)
'''
from urllib import request,error

# 1.设置代理地址
proxy_list = [
    # 用户代理ip集群列表，列表中存放的是dict类型的元素
    {"http":"111.13.134.22:80"},
    {"http":"39.137.77.66:8080"},
    {"http":"39.137.69.7:8080"},
    {"http":"111.63.135.109:80"},
    {"http":"111.13.134.23:80"}
]

# 2.创建ProxyHandler
proxy_handler_list = []
for proxy in proxy_list:
    proxy_handler = request.ProxyHandler(proxy)
    proxy_handler_list.append(proxy_handler)

# 3.创建Opener
opener_list = []
for proxy_handler in proxy_handler_list:
    opener = request.build_opener(proxy_handler)
    opener_list.append(opener)

import random
url = "http://www.baidu.com"

try:
    # 4.安装opener，全局使用
    opener = random.choice(opener_list)
    request.install_opener(opener)

    # 发起请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0'
    }
    req = request.Request(url=url, headers=headers)
    response = request.urlopen(req)
    html = response.read().decode("utf-8")
    print(html)

except Exception as e:
    print(e)
