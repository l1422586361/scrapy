# -*- coding: utf-8 -*-

from scrapy import Spider

class StackSpider(Spider):
    name = 'stack'  # 定义爬虫名称
    allowed_domains = ["stackoverflow.com"] # 定义爬虫可抓取的允许域的基本URL
    start_urls = [
        "http://stackoverflow.com/questions?pagesize=50&sort=newest"    # 定义爬虫开始爬网的URL列表
    ]