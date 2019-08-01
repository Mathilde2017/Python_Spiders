# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 定义自己需要爬行的字段
class XcspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    pass


# 可以自己写一个类
# 定义自己需要爬行的字段

class XiciDailiItem(scrapy.Item):
    # 国家
    country = scrapy.Field()

    # ip地址
    ipaddress = scrapy.Field()

    # 端口
    port = scrapy.Field()

    # 服务器地址
    serveraddr = scrapy.Field()

    # 是否匿名
    isanonymous = scrapy.Field()

    # 类型
    type = scrapy.Field()

    # 存活时间
    alivetime = scrapy.Field()

    # 验证时间
    verifictiontime = scrapy.Field()
