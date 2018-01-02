# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re

import os
from scrapy.exceptions import DropItem


class NovelscrawlerPipeline(object):
    def process_item(self, item, spider):
        if item['title']:
            item['title'] = "".join(item['title']).strip()
            item['article'] = "".join(item['article'])
            item['article'] = build_article_html(item)
            item['file_format'] = item['title'] + ".html"
            save_file(item)
            os.system("open " + item['file_format'])
            return item
        else:
            raise DropItem("Missing title in" % item)


def build_article_html(item):
    # 过略文章中<a> 标签跳转内容
    re_c = re.compile('<\s*a[^>]*>[^<]*<\s*/\s*a\s*>')
    article = re_c.sub("", item['article'])
    # 拼接文章html
    html = '<html><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><div align="center" ' \
           'style="width:100%;text-alight:center"><b><font size="5">' \
           + item['title'] + '</font></b></div>' + article + "</html>"
    return html

def save_file(item):
    fh = open(item['file_format'], 'wb')
    fh.write(item['article'].encode(encoding="utf-8"))
    fh.close()
    pass
