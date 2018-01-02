# encoding:utf-8
import re

import os

import scrapy
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule

from ..items import NovelsrawlerItem


class NovelSpider(CrawlSpider):
    name = 'novel'
    allowed_domains = ['m.book9.net']
    start_urls = ['https://m.book9.net/wapbook/10.html']
    rules = (
        Rule(None, callback='parse'),
    )

    def parse(self, response):
        tag = getattr(self, 'tag', None)
        # 指定的<a>标签的跳转链接
        context = response.xpath('/html/body/div[3]/div[2]/p[1]/a/@href')
        # 获取短链地址
        url = context.extract_first()
        print(url)
        # 请求短链
        yield response.follow(url=url, callback=self.parse_article)

    @staticmethod
    def parse_article(response):
        loader = ItemLoader(NovelsrawlerItem(), response)
        # 生成文章标题
        loader.add_xpath('title', '//*[@id="read"]/div[1]/text()')
        loader.add_xpath('article','//*[@id="chaptercontent"]')
        yield loader.load_item()

