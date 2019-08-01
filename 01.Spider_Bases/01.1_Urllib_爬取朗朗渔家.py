'''
目标：爬取朗朗渔家网站三个页面，并保存下来
    http://langlang2017.com/index.html
    http://langlang2017.com/route.html
    http://langlang2017.com/FAQ.html

技术栈：
    urllib 中的 Request 请求对象
    随机库 random
    伪装请求头 headers 中的 User-Agent
'''

from urllib import request,parse
import random

def spider(url):
    user_agent_list = [
        'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0',
        'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0',
        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'
    ]
    # 随机 user_agent
    user_agent = random.choice(user_agent_list)
    # print(user_agent)

    # 构建header头部信息
    headers = {
        'User-Agent': user_agent
    }

    # 构建请求对象
    rsp = request.Request(url=url,headers=headers)
    response = request.urlopen(rsp)
    html = response.read().decode("utf-8")
    # print(html)

    # 保存文件
    # name = url.split('/')
    # print(name) # ['http:', '', 'langlang2017.com', 'index.html']
    filename = url.split('/')[-1]
    print(filename)
    with open(filename,'w',encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    urls = [
        'http://langlang2017.com/index.html',
        'http://langlang2017.com/route.html',
        'http://langlang2017.com/FAQ.html'
    ]
    for url in urls:
        spider(url)
