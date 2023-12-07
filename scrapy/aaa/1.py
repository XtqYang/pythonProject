from duitangs.items import DuitangsPipeline
from scrapy_redis.spiders import RedisSpider
from scrapy_splash import SplashRequest
import scrapy

# class XiangSpider(RedisSpider):
class XiangSpider(scrapy.Spider):
    name = "xiang"
    allowed_domains = ["duitang.com"]
    start_urls = ["https://www.duitang.com/category/?cat=avatar&sub=男生头像&sub2=&name=男生头像"]
    # redis_key = "ty_start_url"
    # 使用Splash的Lua脚本来滚动页面
    scroll_script = """
    function main(splash, args)
        splash:go(args.url)
        splash:wait(2)
        splash:runjs("window.scrollTo(0, document.body.scrollHeight);")
        splash:wait(2)
        return splash:html()
    end
    """

    """
    重新定义，scrapy原来对于li_list的处理
    只需要重写start_requests()方法
    """
    # def start_requests(self):
    #     cookie_str = """
    #     JSESSIONID=EBD9724103C571131286FAA6C07FBD8F;username=xtq9502;sessionid=a69711bc-d3b7-4f54-beb2-496a56329fde;
    #     """
    #     lst = cookie_str.split(";")
    #     dic = {}
    #     for it in lst:
    #         k, v = it.split("=")
    #         dic[k.strip()] = v.strip()
    #     yield scrapy.Request(
    #         url=self.start_urls[0],
    #         cookies=dic
    #     )
    # url = "https://www.duitang.com/login/"
    # username = "19183320823"
    # password = "hy064872"
    # # 发送post请求的的一个方案
    # yield scrapy.Request(
    #     url=url,
    #     method='post',
    #     body=f"loginName={username}&password={password}",
    #     callback=self.parse
    # )
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, endpoint='execute', args={'lua_source': self.scroll_script})

    def parse(self, resp, **tkwargs):
        li_list = resp.xpath("//div[@class='mbpho']/a[@target='_blank']")
        print(li_list)
        for li in li_list:
            href = li.xpath("./@href").extract_first()
            # 理论上应该开始进行一个网络请求了
            # 根据scrapy的运行原理。此处应该对href进行处理。处理成一个请求。交给引擎
            yield scrapy.Request(
                # 把resp中的url和我刚刚获取的url进行拼接整合
                url=resp.urljoin(href),
                method="get",
                # 回调函数，当响应回馈之后。如何进行处理响应内客
                callback=self.parse_detail
            )
            # 如果这里可以下一页，那么数据解析直接就是当前的这个parse
            next_href = resp.xpath("//div[@class='pages']/ul/li/a[contains(text(),'下一页')]/@href").extract_first()
            if 'next_href':
                yield scrapy.Request(
                    url=resp.urljoin(next_href),
                    callback=self.parse()
                )

    def parse_detail(self, resp, **kwargs):
        img_src = resp.xpath('//div[@class="detail" and @id="pgdetail"]//a[@class="img-out"]/img/@src').extract_first()
        print(img_src)
        item = DuitangsPipeline()
        item['img_src'] = img_src
        yield item