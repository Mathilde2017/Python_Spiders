'''
Urllib登录华为官网：https://www.huawei.com/
url = https://www.huawei.com/en/accounts/LoginPost
method :post
parm:
    userName:18398602437@163.com
    pwd:dTQrjkGfkBIqlHat5e+1ymAEK80RTQH5dCdGca5tXJXcmS8xrha5uV94UfUhLbc4b50JRDFHB/miXtmuFPWZ248mMqz5uyfgAJ+w8J+vO1mAfhFvf9OXJWeZMb/CyvijwzjAlC6mRSHRfblPL5OyCM7X+DVi5MD41LIh5r8EYgc=
    languages:zh
    fromsite:www.huawei.com
    authMethod:password
'''

from urllib import request,parse
from http import cookiejar


# 1.创建 cookiejar 对象
cookie = cookiejar.CookieJar()

# 2.使用 HTTPCookieProcessor 创建cookie处理器
cookie_handler = request.HTTPCookieProcessor(cookie)

# 3.生成http 和https 管理器
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()

# 4.构建发起请求管理器 opener
opener = request.build_opener(cookie_handler,http_handler,https_handler)

# 构建登录函数
def login(url):
    data = {
        "userName":"18398602437@163.com",
        "pwd":"md18398602437",
        "languages":"zh",
        "fromsite":"www.huawei.com",
        "authMethod":"password"
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0'
    }
    data = parse.urlencode(data)
    # data 数据类型为bytes
    req = request.Request(url=url,headers=headers,data=bytes(data,"utf-8"))
    response = opener.open(req)
    html = response.read().decode("utf-8")
    print(html)

if __name__ == '__main__':
    url = "https://www.huawei.com/en/accounts/LoginPost"
    login(url)