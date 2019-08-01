'''
目标：利用正则爬取猫眼电影   http://www.maoyan.com/board

'''
from urllib import request

url = "http://www.maoyan.com/board"

# 1.下载页面内容
rsp = request.urlopen(url)
html = rsp.read().decode("utf-8")
# print(html)

# 2.按 dd 标签提取内容，缩小处理范围
import re
s = r'<dd>(.*?)</dd>'
# ()分组
# 分组的意义，就是在匹配成功的字符串中，在提取()组里面的字符串
pattern = re.compile(s,re.S)
films = pattern.findall(html)
print(len(films))

# 3.从每个 dd 标签中单独提取出需要的信息
for film in films:
    s = r'<a.*?title="(.*?)"'
    pattern = re.compile(s)
    title = pattern.findall(film)[0]
    print(title)