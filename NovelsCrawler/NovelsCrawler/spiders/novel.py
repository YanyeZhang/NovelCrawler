# encoding:utf-8
import re

import os
import scrapy


class NovelSpider(scrapy.Spider):
    name = 'novel'
    allowed_domains = ['m.book9.net']
    start_urls = ['https://m.book9.net/wapbook/10.html']

    def parse(self, response):
        context = response.xpath('/html/body/div[3]/div[2]/p[1]/a/@href')  # 指定的<a>标签的跳转链接
        url = context.extract_first()
        yield response.follow(url=url, callback=self.parse_article)

    def parse_article(self, response):
        print('——————————————')
        title = self.generate_title(response)
        html = self.build_article_html(title, response)
        self.save_file(title + ".html", html)
        os.system("open " + title.replace(" ", "\ ") + ".html")  #用自带的浏览器打开
        pass

    @staticmethod
    def build_article_html(title, response):
        context = response.xpath('//*[@id="chaptercontent"]').extract_first()
        re_c = re.compile('<\s*a[^>]*>[^<]*<\s*/\s*a\s*>')
        article = re_c.sub("", context)  # 过略文章中<a> 标签跳转内容
        html = '<html><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><div align="center" style="width:100%;text-alight:center"><b><font size="5">' \
               + title + '</font></b></div>' + article + "</html>"
        return html

    @staticmethod
    def generate_title(response):
        title = response.xpath('//*[@id="read"]/div[1]/text()').extract()
        return "".join(title).strip()

    @staticmethod
    def save_file(file_name, context):
        fh = open(file_name, 'wb')
        fh.write(context.encode(encoding="utf-8"))
        fh.close()
        pass

