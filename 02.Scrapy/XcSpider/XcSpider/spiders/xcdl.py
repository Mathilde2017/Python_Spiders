# -*- coding: utf-8 -*-
import scrapy
import logging
from XcSpider.items import XiciDailiItem

class XcdlSpider(scrapy.Spider):
    name = 'xcdl'
    allowed_domains = ['xicidaili.com']
    start_urls = ['https://www.xicidaili.com/']

    def parse(self, response):
        items1 = response.xpath('//tr[@class="odd"]')
        items2 = response.xpath('//tr[@class=""]')

        items = items1 + items2
        print(len(items))
        # print(items)
        # 实例化
        infos = XiciDailiItem()
        
        for item in items:
            # 获取国家图片链接
            countries = item.xpath('./td[@class="country"]/img/@src').extract()
            # print(countries) # 列表类型，需要加索引
            if countries != []:
                country = countries[0]
            else:
                country = 'None'
            print(country)

            # 获取 ip 地址
            ipaddress = item.xpath('./td[2]/text()').extract()
            try:
                ipaddress = ipaddress[0]
            except:
                ipaddress = None

            # 获取端口
            port = item.xpath('./td[3]/text()').extract()
            try:
                port = port[0]
            except:
                port = None

            # 获取 服务器地址
            serveraddr = item.xpath('./td[4]/text()').extract()
            try:
                serveraddr = serveraddr[0]
            except:
                serveraddr = ''

            # 是否匿名
            isanonymous = item.xpath('./td[5]/text()').extract()
            try:
                isanonymous = isanonymous[0]
            except:
                isanonymous = None

            # 类型
            type = item.xpath('./td[6]/text()').extract()
            try:
                type = type[0]
            except:
                type = None

            # 存活时间
            alivetime = item.xpath('./td[7]/text()').extract()
            try:
                alivetime = alivetime[0]
            except:
                alivetime = None

            # 验证时间
            verifictiontime = item.xpath('./td[8]/text()').extract()
            try:
                verifictiontime = verifictiontime[0]
            except:
                verifictiontime = None

            # print(country,ipaddress,port,serveraddr,isanonymous,type,alivetime,verifictiontime)
            
            infos['country'] = country
            infos['ipaddress'] = ipaddress
            infos['port'] = port
            infos['serveraddr'] = serveraddr
            infos['isanonymous'] = isanonymous
            infos['type'] = type
            infos['alivetime'] = alivetime
            infos['verifictiontime'] = verifictiontime

            # print(infos)
            
            yield infos
            
            
            