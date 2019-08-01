'''
https://inv-veri.chinatax.gov.cn/index.html 国家税务总局全国增值税发票查验平台
https://www.12306.cn/index/
'''

from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# url = "https://www.12306.cn/index/"
url = "https://inv-veri.chinatax.gov.cn"
headers = {
    'User-Agent':'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0'
}
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
html = response.read().decode()
print(html)