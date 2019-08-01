# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from SunGovDG.items import DongguanItem

class DongguanSpider(CrawlSpider):
    name = 'dongguan'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']
    # 存放定制的获取链接的规则对象（可以是一个列表也可以是元组）
    # 根据规则提取到的所有链接，会由crawlspider构建request对象，并交给引擎处理
    '''
        LinkExtractor : 设置提取链接的规则（正则表达式）
        allow=(), ： 设置允许提取的url
        restrict_xpaths=(), ：根据xpath语法，定位到某一标签下提取链接
        restrict_css=(), ：根据css选择器，定位到某一标签下提取链接
        deny=(), ： 设置不允许提取的url（优先级比allow高）
        allow_domains=(), ： 设置允许提取url的域
        deny_domains=(), ：设置不允许提取url的域（优先级比allow_domains高）
        unique=True, ：如果出现多个相同的url只会保留一个
        strip=True ：默认为True,表示自动去除url首尾的空格
    '''
    '''
    rule
        link_extractor, : linkExtractor对象
        callback=None,  ： 设置回调函数  
        follow=None, ： 设置是否跟进
        process_links=None, ：可以设置回调函数，对所有提取到的url进行拦截
        process_request=identity ： 可以设置回调函数，对request对象进行拦截
    '''
    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )
    # 每个页面的匹配规则
    pagelink = LinkExtractor(allow=('type=4'))
    # print(pagelink)

    # 每个帖子的匹配规则
    contentlink = LinkExtractor(allow=r'/html/question/\d+/\d+.shtml')

    rules = [
        Rule(pagelink,follow=True),
        Rule(contentlink,callback='parse_item')
    ]


    # 注意： CrawlSpider中一定不要出现parse回调方法
    # 由于CrawlSpider使用parse方法来实现其逻辑，如果覆盖了 parse方法，crawl spider将会运行失败。
    def parse_item(self, response):
        # print(response.url)
        item = DongguanItem()
        # title = response.xpath('/html/body/div[9]/table[1]/tbody/tr/td[2]/span[1]').extract()
        title = response.xpath('//span[@class="niae2_top"]/text()')

        number = response.xpath('//div[@class="wzy1"]/table/tr/td[2]/span[2]/text()').extract()[0]
        number = number.split(':')[-1]
        print(number)

        contents = response.xpath('//td[@class="txt16_3"]/text()').extract()

        contents = ''.join(contents)
        contents = contents.replace('\xa0\xa0\xa0\xa0','').replace('\r\n      ','')
        print(contents)









        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item


# 参考：https://www.jianshu.com/p/bc619b0074b0