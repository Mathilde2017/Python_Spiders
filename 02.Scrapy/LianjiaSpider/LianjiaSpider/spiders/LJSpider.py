# -*- coding: utf-8 -*-
import scrapy
import random,time

from LianjiaSpider.settings import headers
from LianjiaSpider.items import LianjiaspiderItem

class LjspiderSpider(scrapy.Spider):
    name = 'LJSpider'
    allowed_domains = ['lianjia.com']
    # start_urls = ['http://lianjia.com/']

    # 重新定义 url 地址
    def start_requests(self):
        # start_urls = []
        # for page in range(1,5):
        #     url = 'https://cd.lianjia.com/zufang/qingyang/pg{}l1rp3/'.format(page)
        #     start_urls.append(url)
        start_urls = [
            'https://cd.lianjia.com/zufang/qingyang/pg1l1rp3/',
            'https://cd.lianjia.com/zufang/pidou/pg1l1rp3/'
        ]
        for start_url in start_urls:
            yield scrapy.Request(url=start_url,callback=self.parse,dont_filter=True,headers=headers)

    def parse(self, response):
        # print(response.body.decode('utf-8'))
        infos = response.xpath('//div[@class="content__list"]/div[@class="content__list--item"]')
        # print(infos)
        for info in infos:
            # 获取房屋标题
            house_titles = info.xpath('.//p[@class="content__list--item--title twoline"]/a/text()').extract()
            # print(house_titles)
            house_title = house_titles[0].strip().replace(' ','')
            # print(house_title)

            # 获取详情链接
            house_hrefs = info.xpath('.//p[@class="content__list--item--title twoline"]/a/@href').extract()
            house_href = 'https://cd.lianjia.com' + house_hrefs[0]
            # print(house_href)

            # 获取小区名称
            house_names = info.xpath('.//p[@class="content__list--item--des"]//a/text()').extract()
            print(house_names)
            house_name = '-'.join(house_names)
            print(house_name)

            # 随机反爬
            time.sleep(random.choice([0.5,2,1,0.35,0.9]))

            yield scrapy.Request(url=house_href,callback=self.detail_parse,dont_filter=True,headers=headers,meta={'house_title':house_title,'house_href':house_href,'house_name':house_name})


    def detail_parse(self,response):
        infos = response.xpath('//div[@class="content clear w1150"]')

        for info in infos:
            # 房源编号
            house_nums = info.xpath('.//i[@class="house_code"]/text()').extract()
            print(house_nums)
            house_num = house_nums[0].split(': ')[-1]

            # 房屋价格
            house_prices = info.xpath('.//p[@class="content__aside--title"]/span/text()').extract()
            house_price = house_prices[0] + '元/月'


            # 进行数据存储
            item = LianjiaspiderItem()

            # 以下3个数据 是通过 meta 传过来的。
            item['house_title'] = response.meta['house_title']
            item['house_href'] = response.meta['house_href']
            item['house_name'] = response.meta['house_name']

            item['house_num'] = house_num
            item['house_price'] = house_price

            yield item

