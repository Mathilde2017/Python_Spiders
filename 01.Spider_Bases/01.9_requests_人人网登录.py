import requests

# 1、创建 session 对象，可以保存 Cookie 值
sess = requests.session()

# 2、处理 headers
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

# 3、需要登录的用户和密码
data = {"email":"18398602437","password":"md18398602437"}

# 4、发送附带用户名和密码的请求，并获取登录后的 cookie值，存在 sess 里
sess.post("http://www.renren.com/PLogin.do",data=data)

# 5、sess 里面包含用户登录后的 Cookie值，可以直接访问那些登录后才可以访问的页面
response = sess.get("http://www.renren.com/971531208")

print(response.text)