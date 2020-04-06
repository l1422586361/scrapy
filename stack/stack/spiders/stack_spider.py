# -*- coding: utf-8 -*-

from scrapy import Spider

# class StackSpider(Spider):
#     name = 'stack'  # 定义爬虫名称
#     allowed_domains = ["stackoverflow.com"] # 定义爬虫可抓取的允许域的基本URL
#     start_urls = [
#         "http://stackoverflow.com/questions?pagesize=50&sort=newest"    # 定义爬虫开始爬网的URL列表
#     ]

#     def parse(self,response):
#         questions = Selector(response).xpath('//div[@class="summary"]/h3')

#         for question in questions:
#             itm = StackItem()
#             item['title'] = question.xpath('a[@class = "question-hyperlink"]/text()').extract()[0]
#             item['url'] = question.xpath('a[@class = "question-hyperlink"]/@href').extract()[0]
#             yield item

class StackSpider(Spider):
    name = 'stack'  # 定义爬虫名称
    allowed_domains = ["stackoverflow.com"] # 定义爬虫可抓取的允许域的基本URL
    start_urls = [
        "https://www.bilibili.com/ranking?spm_id_from=333.851.b_7072696d61727950616765546162.3"    # 定义爬虫开始爬网的URL列表
    ]

    def parse(self,response):
        questions = Selector(response).xpath('//div[@class="info"]/h3')

        for question in questions:
            itm = StackItem()
            item['title'] = question.xpath('a[@class = "title"]/text()').extract()[0]
            item['url'] = question.xpath('a[@class = "title"]/@href').extract()[0]
            yield item

    # //*[@id="question-summary-61061485"]/div[2]


