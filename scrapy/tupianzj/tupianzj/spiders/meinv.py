import scrapy
from tupianzj.items import MeinvItem


class MeinvSpider(scrapy.Spider):
    name = "meinv"
    allowed_domains = ["tupianzj.com"]
    start_urls = ["https://www.tupianzj.com/bizhi/DNmeinv/"]

    def parse(self, resp, **tkwargs):
        li_list = resp.xpath("//ul[@class='list_con_box_ul']/li")
        for li in li_list:
            href = li.xpath("./a/@href").extract_first()
            # 理论上应该开始进行一个网络请求了
            # 根据scrapy的运行原理。此处应该对href进行处理。处理成一个请求。交给引擎
            yield scrapy.Request(
                # 把resp中的url和我刚刚获取的url进行拼接整合
                url=href.urljoin(href),
                method="get",
                # 回调函数，当响应回馈之后。如何进行处理响应内客
                callback=self.parse_detail
            )
            # 如果这里可以下一页，那么数据解析直接就是当前的这个parse
            next_href = resp.xpath("//div[@class='pages']/ul/li/a[contains(text(),'下一页')]/@href").extract_first()
            if next_href:
                yield scrapy.Request(
                    url=resp.urljoin(next_href),
                    callback=self.parse()
                )

    def parse_detail(self, resp, **kwargs):
        name = resp.xpath('//*[@id="container"]/div/div/div[2]/h1/text()').extract()
        img_src = resp.xpath("//div[@id='bigpic]/a/img/@src")
        item = MeinvItem()
        item['name'] = name
        item['img_src'] = img_src
        print(img_src)
        yield item
