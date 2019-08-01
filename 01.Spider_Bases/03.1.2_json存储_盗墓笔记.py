import requests,json
from bs4 import BeautifulSoup

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}
url = "http://www.seputu.com/"

rsp = requests.get(url,headers)
# print(rsp.text)

soup = BeautifulSoup(rsp.text,'lxml')
content = []
# 注意：class 在Python中是保留字, 使用 class 做参数会导致语法错误.
# 从Beautiful Soup的4.1.1版本开始, 可以通过 class_  参数搜索有指定CSS类名的tag
for mulu in soup.find_all(class_="mulu"):
    # 标题
    h2 = mulu.find('h2')
    # print(h2)   # 有None值存在
    list = []
    if h2 !=None:
        h2_title = h2.string

        # 章节内容及url地址
        for a in mulu.find(class_="box").find_all("a"):
            href = a.get('href')
            box_title = a.get('title')
            print(href,box_title)
            list.append({'href':href,'box_title':box_title})
        content.append({'title':h2_title,'content':list})

with open('gcd.json','w',encoding='utf-8') as f:
    json.dump(content,fp=f,indent=4,ensure_ascii=False)
    # 注意：ensure_ascii=False 解决中文问题，其中 False 首字母一定大写，不能小写！
    # indent：是缩放



