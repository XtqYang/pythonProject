import scrapy
from scrapy_redis.spiders import RedisSpider
from duitang_com.items import ImgsproItem
import json


class TianyaApiSpider(RedisSpider):
    name = "tianya_api"
    allowed_domains = ["duitang.com"]
    redis_key = "start_urls"  # 修改为适当的队列名称
    redis_encoding = 'utf-8'

    def __init__(self, *args, **kwargs):
        super(TianyaApiSpider, self).__init__(*args, **kwargs)

    # def start_requests(self):
    #     pass

    def parse(self, response, **kwargs):
        # 下载的路径
        meta_data = response.meta.get("path")
        i = 0
        # 检查响应的内容类型
        content_type = response.headers.get('Content-Type').decode('utf-8')
        if 'application/json' not in content_type:
            # 如果响应不是JSON，直接返回
            return
        data = json.loads(response.text)
        paths = []
        for obj in data["data"]["object_list"]:
            if "photo" in obj:
                paths.append(obj["photo"]["path"])
        for dt_src in paths:
            i = i + 1
            print(f"正在下载第{i}个")
            # 将数据转换为JSON字符串并推送到Redis队列中
            # data = {'url': dt_src}
            # json_data = json.dumps(data)
            # self.server.lpush('start_urls', json_data)
            # 下载
            tian = ImgsproItem()
            tian['img_src'] = dt_src
            tian['path'] = meta_data
            yield tian
