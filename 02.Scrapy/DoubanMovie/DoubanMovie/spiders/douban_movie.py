# -*- coding: utf-8 -*-
import scrapy
from DoubanMovie.items import DoubanmovieItem


class DoubanMovieSpider(scrapy.Spider):
    name = 'douban_movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/']

    def parse(self, response):
        item = DoubanmovieItem()
        
        pass
