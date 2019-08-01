'''
博客园首页：https://www.cnblogs.com/
本案例主讲 bs4 css选择器， select 的用法
bs4 还有 find findall find_previous...

'''

import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "cache-control" : "public, max-age=21"
}
url = "https://www.cnblogs.com/cate/python/"
html = requests.get(url,headers)
# print(html.text)

soup = BeautifulSoup(html.text,'lxml')
items = soup.select('div[class="post_item_body"]')
# print(items)

for item in items:
    # 标题
    title = item.select('h3 a[class="titlelnk"]')[0].get_text()
    # title2 = item.select('h3 a[class="titlelnk"]')
    # print(title2)
    # print(type(title2)) # 返回 <class 'list'>，所以上面要加索引 [0] ！后面的同理！
    # print(title)

    # 详情链接
    href = item.select('h3 a[class="titlelnk"]')[0]['href']     # 两种获取属性的方式
    # 作者名字
    author = item.select('div a[class="lightblue"]')[0].get_text()
    # print(author)
    # 作者主页链接
    author_home = item.select('div a[class="lightblue"]')[0].get('href')  # 两种获取属性的方式
    # print(author_home)
    # 简要信息
    summary = item.select('p[class="post_item_summary"]')[0].get_text().strip('\n').strip(' ').strip('\r\n')
    # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
    # 注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
    # print(summary)

    datas = item.select('div[class="post_item_foot"]')[0].get_text()
    # print(datas,type(datas))
    datas = datas.split(' ')
    # split() 通过指定分隔符对字符串进行切片，如果参数 num，有指定值，则分隔 num + 1个子字符串
    # print(datas,type(datas))
    # ['\n吃鸡吗？带带我', '\r\n', '', '', '', '发布于', '2019-07-19', '01:29', '\r\n', '', '', '', '\r\n', '', '', '', '', '', '',
    #  '', '评论(0)阅读(12)']

    # 时间
    time = datas[6] + ' ' + datas[7]

    # 评论
    comment = datas[-1].lstrip('评论(').rstrip(')')[0]
    # print(comment)
    # 阅读数
    read_num = datas[-1].lstrip('评论(').rstrip(')').strip('(')[-1]
