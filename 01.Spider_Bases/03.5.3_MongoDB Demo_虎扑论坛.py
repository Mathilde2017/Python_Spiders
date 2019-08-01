
import requests
from lxml import etree


# 1、获取初始页面信息
def spider(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }

    res = requests.get(url,headers=headers)
    html = res.text
    # print(html)
    html = etree.HTML(html)
    return html

# 2、解析页面信息
def parse(html):
    # 标题
    titles = html.xpath('//ul[@class="for-list"]//div[@class="titlelink box"]/a[@class="truetit"]/text()')
    # print(titles)

    # 详情页面链接
    parse_hrefs = html.xpath('//ul[@class="for-list"]//div[@class="titlelink box"]/a[@class="truetit"]/@href')
    parse_hrefs = ['https://bbs.hupu.com' + href for href in parse_hrefs]
    # print(parse_hrefs)

    # 获取标题
    titles = []
    for href in parse_hrefs:
        titles.append(title(href))

    # 获取作者
    authors = html.xpath('//div[@class="author box"]/a[@class="aulink"]/text()')
    # print(authors)

    # 获取发布时间
    times = html.xpath('//div[@class="author box"]/a[2]/text()')
    # print(times)

    # 获取回复数和浏览数
    datas = html.xpath('//ul[@class="for-list"]/li/span[@class="ansour box"]/text()')
    # print(datas)
    datas = [x.split('\xa0/\xa0') for x in datas]
    # print(datas)

    # 回复数
    replies = [x[0] for x in datas]
    # 浏览数
    browses = [x[1] for x in datas]
    # print(replies)
    # print(browses)

    # 最后回复时间
    last_times = html.xpath('//div[@class="endreply box"]/a/text()')

    # 最后回复人
    last_names = html.xpath('//div[@class="endreply box"]/span[@class="endauthor "]/text()')
    print(last_names)
    # print(last_times)
    print(len(titles),len(parse_hrefs),len(authors),len(times),len(replies),len(browses),len(last_times),len(last_names))

def title(href):
    html = spider(href)
    try:
        t = html.xpath('//div[@class="bbs-hd-h1"]/h1/text()')[0]
    except:
        t = "未知参数，请确认"
    # return t
    print(t)



def main():
    url = "https://bbs.hupu.com/nba-5"
    html = spider(url)
    parse(html)

if __name__=='__main__':
    main()
