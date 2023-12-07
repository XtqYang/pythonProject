from urllib import response
from scrapy_dangdang.items import ScrapyDangdangItem
import scrapy


class DangSpider(scrapy.Spider):
    name = 'dang'
    allowed_domains = ['book.dangdang.com']
    start_urls = ['http://book.dangdang.com/']

    # base_url = 'http://book.dangdang.com/pg'
    # page = 1

    def parse(self, response):
        # pipelines 下载数据
        # items 定义数据结构
        # name_list = response.xpath('//ul[@id="component_403754__5298_5294__5294"]/li/a/img/@src')  # 图片
        # price_list = response.xpath('//ul[@id="component_403754__5298_5294__5294"]/li/a/@title')  # 名字
        # price_list = response.xpath('//ul[@id="component_403754__5298_5294__5294"]/li/p/span/span[@class="num"]')  # 价格
        # 新写法
        li_list = response.xpath('//ul[@id="component_403754__5298_5294__5294"]/li')

        for li in li_list:
            src = li.xpath('./a/img/@src').extract_first()  # 图片
            name = li.xpath('./a/@title').extract_first()  # 名字
            price = li.xpath('./p/span/span[@class="num"]/text()').extract_first()  # 价格
            # pipelines 下载数据
            book = ScrapyDangdangItem(src=src, name=name, price=price)
            # 获取一个book就将book交给pipelines
            yield book

        # 多页下载
        # if self.page < 100:
        #     self.page = self.page + 1
        #     url = self.base_url + str(self.page) + '-cp01.01.02.00.00.00.html'
        #     yield scrapy.Request(url=url, callback=self.parse)
