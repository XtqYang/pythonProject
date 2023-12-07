import scrapy


class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['www.autohome.com.cn']
    # 后缀为html时后面不允许加/
    start_urls = ['https://www.autohome.com.cn/car/']

    def parse(self, response):
        name_list = response.xpath('//*/h4/a/text()')  # 汽车名
        price_list = response.xpath('//*[@class="red"]/text()')  # 汽车价格
        for i in range(len(name_list)):
            name = name_list[i].extract()
            price = price_list[i].extract()
            # extract()提取seletor对象的data属性值
            print(name, price)

# 1、引擎：怎么样，爬虫老弟，搞起来啊！
# 2、Spider：好啊，老哥，来来来，开始吧。今天就爬xxx网站怎么样
# 3、引擎：没问题，入口URL发过来！
# 4、Spider：呐，入口URL是https://ww.xxx.com。
# 5、引擎：调度器老弟， 我这有request请求你帮我排序入队一下吧。
# 6、调度器：引擎老哥，这是我处理好的request。
# 7、引擎：下载器老弟，你按照下载中间件的设置帮我下载一下这个request请求。
# 8、下载器：可以了，这是下载好的东西。（如果失败：sorry，这个request下载失败了。然后引擎告诉调度器，这个request下载失败了，你记录一下，我们待会儿再下载）
# 9、引擎：爬虫老弟，这是下载好的东西，下载器已经按照下载中间件处理过了，你自己处理一下吧。
# 10、Spider：引擎老哥，我的数据处理完毕了，这里有两个结果，这个是我需要跟进的URL，还有这个是我获取到的Item数据。
# 11、引擎：管道老弟，我这儿有个item你帮我处理一下！
# 12、引擎：调度器老弟，这是需要跟进URL你帮我处理下。（然后从第四步开始循环，直到获取完需要全部信息
# ————————————————
# 版权声明：本文为CSDN博主「可爱丸学python」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/qq_34120459/article/details/86711728
