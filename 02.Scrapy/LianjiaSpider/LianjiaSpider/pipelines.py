# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from openpyxl import Workbook

class LianjiaspiderPipeline(object):
    def process_item(self, item, spider):
        return item

# 一、Json 存储
class LianjiaSpiderJsonPipeline(object):
    def __init__(self):
        self.file = open('lijian.json','w',encoding='utf-8')

    def process_item(self, item, spider):
        str = json.dumps(dict(item),ensure_ascii=False)
        str = str +'\n'

        self.file.write(str)
        return item

    def close_spider(self,spider):
        self.file.close()

    # 去 setting 中开启 pipeline


# 二、Excel 存储
# https://www.cnblogs.com/zeke-python-road/p/8986318.html
class LianjiaSpiderExcelPipeline():
    def __init__(self):
        self.wb = Workbook()    #创建文件对象
        self.ws = self.wb.active  # 获取第一个sheet
        self.ws.append(['house_title','house_href','house_name','house_num','house_price'])

    def process_item(self, item, spider):
        line = [item['house_title'],item['house_href'],item['house_name'],item['house_num'],item['house_price']]
        self.ws.append(line)
        self.wb.save('lianjia.xlsx')

        return item


    # 去 setting 中开启 pipeline


# 三、MySQL 存储
# 将 西刺代理 代码 拷贝过来即可，建数据库，改字段