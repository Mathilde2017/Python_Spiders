import requests

url = "http://www.baidu.com/s?"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}
kw = {
    'wd':'python'
}
# params 接收一个字典或者字符串查询参数，字典类型自动转换为 url 编码，不再需要 urlopen() 方法
rsp = requests.get(url,params=kw,headers=headers)

print(rsp.text)
print(rsp.content)
print(rsp.status_code)
print(rsp.url)
print(rsp.encoding) # 指从HTTP的header中猜测的响应内容编码方式，如果header中不存在charset，则默认编码为ISO-8859-1
print(rsp.headers)
print(rsp.cookies)
print(rsp.apparent_encoding) # 原文编码类型
rsp.encoding = rsp.apparent_encoding # 解决页面乱码问题
# 返回 cookie 对象
cookiejar = rsp.cookies
# 将 cookiejar 转为字典
cookie_dict = requests.utils.dict_from_cookiejar(cookiejar)
print(cookiejar)
print(cookie_dict)