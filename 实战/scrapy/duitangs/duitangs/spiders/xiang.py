from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from duitangs.items import DuitangsPipeline
from scrapy_redis.spiders import RedisSpider
from selenium.webdriver.common.by import By
from selenium import webdriver
import scrapy
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')

class XiangSpider(RedisSpider):
    name = "xiang"
    allowed_domains = ["duitang.com"]
    # 删除start_urls
    # start_urls = ["https://www.duitang.com/category/?cat=avatar&sub=男生头像&sub2=&name=男生头像#!hot-p1"]
    redis_key = "start_urls"  # 修改redis_key的值
    def __init__(self, *args, **kwargs):
        super(XiangSpider, self).__init__(*args, **kwargs)
        chrome_path = 'D:/code/pythonProject/scrapy/chromedriver.exe'
        options = webdriver.ChromeOptions()
        service = ChromeService(executable_path=chrome_path)
        self.driver = webdriver.Chrome(options=options, service=service)
        self.count = 0  # 初始化计数器

    def check_browser(self):
        try:
            self.driver.current_url
        except NoSuchWindowException:
            chrome_path = 'D:/code/pythonProject/scrapy/chromedriver.exe'
            options = webdriver.ChromeOptions()
            service = ChromeService(executable_path=chrome_path)
            self.driver = webdriver.Chrome(options=options, service=service)

    def start_requests(self):
        # 从Redis队列中读取URL，无需自己指定start_urls
        return
    # def start_requests(self):
    #     for url in self.start_urls:
    #         self.check_browser()
    #         self.driver.get(url)
    #         # 直接调用parse_response方法，而不是return
    #         yield from self.parse_response()
    def scroll_to_end(self):
        # 循环滚动到页面底部
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            print("滑动中...")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)  # 等待页面加载
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def parse_response(self, response=None):
        print("执行N")
        if response:
            self.driver.get(response.url)

        self.check_browser()
        try:
            wait = WebDriverWait(self.driver, 5)
            close_btn = wait.until(EC.presence_of_element_located((By.XPATH, '//a[@class="mask-close"]')))
            close_btn.click()
            time.sleep(1)
        except NoSuchElementException as e:
            print("未找到关闭按钮:")

        while True:
            self.scroll_to_end()

            page_source = self.driver.page_source
            sel_response = scrapy.http.HtmlResponse(url=self.driver.current_url, body=page_source, encoding="utf-8")

            a_elements = sel_response.xpath('//a[@target="_blank" and @class="a"]')
            for a_element in a_elements:
                self.count += 1
                href = a_element.xpath('./@href').extract_first()
                yield scrapy.Request(url=sel_response.urljoin(href), method="get", callback=self.parse_detail)

            next_button = self.driver.find_elements(By.XPATH, '//a[@class="woo-nxt"][@pdir]')
            for button in next_button:
                pdir_value = button.get_attribute('pdir')
                if pdir_value == "1":
                    print("翻页")
                    try:
                        button.click()
                        # Wait for the new page to load fully
                        WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '//a[@class="woo-nxt"][@pdir]')))
                    except TimeoutException as e:
                        print("无弹窗，继续执行")
                    # 继续下一个循环，处理新页面
                else:
                    break  # 退出循环，没有下一页按钮了
    def parse_detail(self, response):
        img_src = response.xpath(
            '//div[@class="detail" and @id="pgdetail"]//a[@class="img-out"]/img/@src').extract_first()
        print(img_src)
        item = DuitangsPipeline()
        item['img_src'] = img_src
        yield item

    def close(self, reason):
        print(f"总共抓取: {self.count}" + "条数据")  # 打印总数
        self.driver.quit()
