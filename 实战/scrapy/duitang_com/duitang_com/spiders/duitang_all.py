import os
import time
import redis
import scrapy
from scrapy_redis.spiders import RedisSpider
from duitang_com.items import DuitangComItem
import json

count = 0


class DuitangAllSpider(scrapy.Spider):
    # 添加两个类属性来跟踪和限制推送次数
    push_count = 0
    MAX_PUSHES = 5  # 你可以根据需要更改这个值
    name = 'duitang_all'
    allowed_domains = ['duitang.com']
    start_urls = ['https://www.duitang.com/topics/']

    # 大分类，23个
    def parse(self, response):
        nav_links = response.css('#dt-nav-bottom .dt-nav-group a')
        for link in nav_links:
            href = link.attrib['href']
            text = link.css('::text').get()
            if href:
                full_url = f"https://www.duitang.com{href}"
                yield scrapy.Request(url=full_url, callback=self.parse_link)

    def parse_link(self, response):
        # 处理大分类
        global count
        nav_links = response.xpath("//h2[@class='dt-cat-title']/text()")
        for text in nav_links:
            value = text.get().strip()
            folder_path_lvl1 = os.path.join(os.getcwd(), "meinvtupian", value)
            if not os.path.exists(folder_path_lvl1):
                os.makedirs(folder_path_lvl1)

            # 处理与当前大分类相关的小分类
            nav_links2 = response.xpath("//div[@class='dt-sub-cat-name']/text()")
            i = 0
            _ = 1694863160223
            start = 0
            for text2 in nav_links2:
                value2 = text2.get().strip()
                folder_path_lvl2 = os.path.join(folder_path_lvl1, value2)
                if not os.path.exists(folder_path_lvl2):
                    os.makedirs(folder_path_lvl2)
                # 处理与当前小分类相关的标签
                nav_links3 = response.xpath("//div[@class='dt-tag-list clr']/a/text()")

                for text3 in nav_links3:
                    value3 = text3.get().strip()
                    folder_path_lvl3 = os.path.join(folder_path_lvl2, value3)
                    if not os.path.exists(folder_path_lvl3):
                        os.makedirs(folder_path_lvl3)
                    while i < 30:
                        count = 1 + count
                        i = i + 1
                        start = start + 24
                        _ = _ + 1
                        port = f"https://www.duitang.com/napi/blog/list/by_search/?include_fields=like_count,sender,album,msg,reply_count,top_comments&kw={value3}&start={start}&_={_}"
                        print(value3 + f"第{i}个已推送:" + port)
                        print("共计" + count.__str__() + "个")
                        print(folder_path_lvl3)
                        self._redis(folder_path_lvl3, port, i)

    def _redis(self, path, port, i):
        # 检查是否已达到最大推送次数
        # if DuitangAllSpider.push_count >= DuitangAllSpider.MAX_PUSHES:
        #     return
        # 创建 Redis 连接
        r = redis.StrictRedis(host='localhost', port=6379, db=8)
        # 创建请求数据
        request_data = {
            "url": port,
            "meta": {
                "path": path,
            },
        }
        # 将请求数据转换为 JSON 格式并推送到 Redis 列表
        r.lpush('start_urls', json.dumps(request_data))
        print("路径:" + request_data["meta"]["path"])
        print(f"第{i + 1}个已推送:" + request_data["url"])
        time.sleep(2)
        DuitangAllSpider.push_count += 1
