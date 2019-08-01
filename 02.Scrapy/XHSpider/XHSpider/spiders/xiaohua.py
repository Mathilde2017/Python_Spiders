# -*- coding: utf-8 -*-
'''
爬取校花网
学习目标：
    - 下载中间件的初步使用
    - scrapy 简单对接 selenium
'''
import scrapy
from XHSpider.items import XhspiderItem

class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/2014.html']

    def parse(self, response):
        infos = response.xpath('//div[@class="items"]')
        # print(infos)
        for info in infos:
            # print(info)
            title = info.xpath('.//p/a/text()').extract()[0]
            href = info.xpath('.//p/a/@href').extract()[0]
            href = "http://www.xiaohuar.com/" + href.split('/')[-1]

            item = XhspiderItem()
            item['title'] = title
            item['href'] = href

            yield item
