'''
此文件主要作用是在 pycharm 运行爬虫
'''
from scrapy import cmdline

cmdline.execute('scrapy crawl xcdl'.split())