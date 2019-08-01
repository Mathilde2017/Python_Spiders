# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from XcSpider import settings

class XcspiderPipeline(object):
    def process_item(self, item, spider):
        return item

class XcMongoPipeline(object):
    def __init__(self):
        host = settings.MongoDB_HOST
        port = settings.MongoDB_PORT
        dbname = settings.MongoDB_DBNAME
        sheetname = settings.MongoDB_SHEETNAME

        # 创建 MONGODB 数据库连接
        client = pymongo.MongoClient(host=host,port=port)

        # 指定数据库
        mydb = client[dbname]

        # 存放数据的数据库表名
        self.post = mydb[sheetname]

    def process_item(self,item,spider):
        data = dict(item)
        self.post.insert(data)
        print('插入成功')
        return item
    