'''
百度翻译是：AJAX请求；返回值：json 数据
请求地址：https://fanyi.baidu.com/sug
构建参数：kw:hi

注意请求头信息：
content-length:5  如：kw=hi
此处先将 kw 参数编码，再用 len 求长度
'''
from urllib import request,parse
import json

def BaiduFanyi(content):
    # 封装关键词
    data = {
        'kw':content
    }

    data = parse.urlencode(data)

    url = "https://fanyi.baidu.com/sug"

    headers = {
        "content-length" : len(data),
        "user-agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }

    req = request.Request(url=url,data=bytes(data,encoding="utf-8"),headers=headers)
    response = request.urlopen(req)
    html = response.read().decode("utf-8")
    print(html)

    # json.loads()
    # 函数是将json格式数据转换为字典（可以这么理解，json.loads()
    # 函数是将字符串转化为字典）
    json_data = json.loads(html)
    for item in json_data['data']:
        print(item)

    print(json_data)

if __name__ == "__main__":
    content = input("请输入需要翻译的单词：")
    BaiduFanyi(content)