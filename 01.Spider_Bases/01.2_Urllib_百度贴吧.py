'''
目标：爬取百度贴吧
分析：
    http://tieba.baidu.com/f?kw=python
    http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50
    http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=100
    得出规律：
    kw参数需要转码；
    每一页只有后面数字不同，且数字是(页数-1)*50。
方法：
    1.准备构建参数字典：
        字典包含三部分：kw ie pn
    2.使用用parse构建完整的url  parse.urlencode()
    3.使用for循环下载

'''
from urllib import request,parse

url = "http://tieba.baidu.com/f?"
kw = input('请输入贴吧名字：')
pn = int(input('请输入查询页码：'))

for i in range(pn):
    qs = {
        'kw' : kw,
        'ie' : 'utf-8',
        'pn' : i*50
    }

    qs_data = parse.urlencode(qs)
    url = url + qs_data
    print(url)

    headers = {
        'User-Agent':'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0'
    }
    req = request.Request(url=url,headers=headers)
    response = request.urlopen(req)
    html = response.read().decode("utf-8")
    print(html)

    # 保存文件
    # with open(kw + "第" + str(i+1) + "页" + ".html", 'w', encoding="utf-8") as f:
    #     f.write(html)
