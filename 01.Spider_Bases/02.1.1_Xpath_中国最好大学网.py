'''
url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html"
'''

from urllib import request
from lxml import etree

url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html"
respose = request.urlopen(url)
html = respose.read().decode()
# print(html)

# etree.HTML():构造了一个XPath解析对象并对HTML文本进行自动修正。
# etree.tostring()：输出修正后的结果，类型是bytes
html = etree.HTML(html)

items = html.xpath('//tr[@class="alt"]')
# print(items)

for item in items:
    # 排名
    number = item.xpath('./td')[0].text
    # 学校
    school = item.xpath('.//div[@align="left"]')[0].text
    # 省份
    addr = item.xpath('./td')[2].text
    # 总分
    score = item.xpath('./td')[3].text
    
    print(number + "---" +school + "---" +addr + "---" +score)