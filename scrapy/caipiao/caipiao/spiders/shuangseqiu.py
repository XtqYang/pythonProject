import scrapy
from caipiao.items import CaipiaoItem


class ShuangseqiuSpider(scrapy.Spider):
    name = "shuangseqiu"
    allowed_domains = ["500.com"]
    start_urls = ["https://datachart.500.com/ssq/"]

    # 形参名字随便改
    def parse(self, resp, **kwargs):
        xpath = resp.xpath("//tbody[@id='tdata']//tr")
        for tr in xpath:
            # 过滤空数据
            if tr.xpath("./@class").extract_first() == "tdbck":
                continue
            # scrapy支持xpath和css混着用
            '''
            使用xpath
            red_ball = tr.xpath(".//td[@class='chartBall01']/text()").extract()
            使用css
            red_ball = tr.css(".chartBall01::text").extract()
            '''
            # 红球
            red_ball = tr.css(".chartBall01::text").extract()
            # 蓝球
            blue_ball = tr.css(".chartBall02::text").extract_first()
            # 期号
            # strip()用于去除字符串两端的空格（包括空格、制表符、换行符等空白字符）
            qihao = tr.xpath("./td[1]/text()").extract_first().strip()
            # #########################管道#########################
            # 不要这样使用
            '''
            dic = {
                "qihao": qihao,
                "red_ball": red_ball,
                "blue_ball": blue_ball
            }
            '''
            # 定义字典
            cai = CaipiaoItem()
            cai['qihao'] = qihao
            cai['red_ball'] = red_ball
            cai['blue_ball'] = blue_ball
            yield cai
