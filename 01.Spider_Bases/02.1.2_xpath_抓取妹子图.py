import requests
from lxml import etree

def mz_parse(base_url,headers):
    res = requests.get(base_url,headers)
    html = etree.HTML(res.text)

    # 获取详情信息
    img_src = html.xpath('')
    for img_url in img_src:
        img_parse(img_url)

def img_parse(img_url):
    res = requests.get(img_url)
