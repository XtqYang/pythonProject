import scrapy

# 电影天堂多层爬取
# 要第一页的名字和第二页的图片
from scrapy_movieTT.pipelines import ScrapyMoviettPipeline


class MvSpider(scrapy.Spider):
    name = 'mv'
    allowed_domains = ['www.dytt8.net']
    start_urls = ['https://dytt8.net/html/gndy/china/index.html']

    def parse(self, response):
        a_list = response.xpath('//div[@class="co_content8"]//td[2]//a[2]')

        for a in a_list:
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()
            # 第二页的地址是
            url = 'https://dytt8.net' + href
            # 对第二页的链接发起访问
            yield scrapy.Request(url=url, callback=self.parse_second, dont_filter=True, meta={'name': name})

    def parse_second(self, response):
        # 如果拿不到数据，一定检查xpath语法是否正确
        src = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        # 接收到请求的meta参数值
        name = response.meta['name']
        movie = ScrapyMoviettPipeline(src=src, name=name)
        yield movie
#  ScrapyMoviettPipeline()不接受参数