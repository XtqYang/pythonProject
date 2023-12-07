# import scrapy
# from scrapy_selenium import SeleniumRequest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from scrapy.signals import spider_closed
# import time
# from duitangs.items import DuitangsPipeline
#
#
# class XiangSpider(scrapy.Spider):
#     name = "xiang"
#     allowed_domains = ["duitang.com"]
#     start_urls = ["https://www.duitang.com/category/?cat=avatar&sub=男生头像&sub2=&name=男生头像"]
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         chrome_path = 'D:\\code\\pythonProject\\scrapy\\chromedriver.exe'
#         options = webdriver.ChromeOptions()
#         service = ChromeService(executable_path=chrome_path)
#         self.driver = webdriver.Chrome(options=options, service=service)
#         self.count = 0  # 初始化计数器
#
#     def start_requests(self):
#         for url in self.start_urls:
#             yield SeleniumRequest(url=url, callback=self.parse)
#
#     def parse(self, response):
#         # 使用Selenium打开和滚动网页
#         self.driver.get(response.url)
#         last_height = self.driver.execute_script("return document.body.scrollHeight")
#         while True:
#             self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#             time.sleep(1)
#             new_height = self.driver.execute_script("return document.body.scrollHeight")
#             if new_height == last_height:
#                 break
#             last_height = new_height
#
#         for i in range(120):
#             print(1)
#             xpath_expression = r'//*[@id="woo-holder"]/div[1]/div[2]/div[{i}]/div/div[1]/a/@href'
#             href_values = response.xpath(xpath_expression)
#             print(2)
#             if href_values:
#                 # 打印匹配到的href值
#                 for href in href_values:
#                     print(href)
#
#         li_list = response.xpath('//*[@class="mbpho"]/a[starts-with(@href, "/blog/?id=")]')
#         for li in li_list:
#             self.count += 1
#             href = li.xpath("./@href").extract_first()
#             print(href)
#             yield scrapy.Request(
#                 url=response.urljoin(href),
#                 method="get",
#                 callback=self.parse_detail
#             )
#
#         # 如果这里可以下一页，那么数据解析直接就是当前的这个parse
#         next_href = response.xpath("//div[@class='pages']/ul/li/a[contains(@href, 'pdir=-1')]/@href").extract_first()
#         # next_href = response.xpath("//div[@class='pages']/ul/li/a[contains(text(),'下一页')]/@href").extract_first()
#         if next_href:
#             yield scrapy.Request(
#                 url=response.urljoin(next_href),
#                 callback=self.parse()
#             )
#
#     def parse_detail(self, response):
#         img_src = response.xpath(
#             '//div[@class="detail" and @id="pgdetail"]//a[@class="img-out"]/img/@src').extract_first()
#         print(img_src)
#         item = DuitangsPipeline()
#         item['img_src'] = img_src
#         yield item
#
#     def spider_closed_handler(self, spider):
#         """当爬虫关闭时调用的处理器函数"""
#         self.driver.quit()
#         print(f"共计有: {self.count}")  # 打印总数
