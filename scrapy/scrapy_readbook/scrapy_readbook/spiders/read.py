# 创建项目 scrapy startproject 项目名字
# 创建爬虫文件 scrapy genspider -t crawl 爬虫文件名字 爬取的域名
# 运行 scrapy crawl read
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy_readbook.items import ScrapyReadbookItem


class ReadSpider(CrawlSpider):
    name = 'read'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1188.html']

    rules = (
        Rule(LinkExtractor(allow=r'/book/1188_\d+\.html'),
             callback='parse_item',
             follow=False),
    )

    def parse_item(self, response):
        img_list = response.xpath('//div[@class="bookslist"]//img')
        for img in img_list:
            name = img.xpath('./@data-original').extract_first()
            src = img.xpath('./@alt').extract_first()
            book = ScrapyReadbookItem(name=name, src=src)
            yield book
