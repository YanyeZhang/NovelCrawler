# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelsrawlerItem(scrapy.Item):
    title = scrapy.Field()
    article = scrapy.Field()
    file_format = scrapy.Field()
    pass
