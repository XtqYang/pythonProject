# Define your item pipelines here
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface
import urllib.request

from itemadapter import ItemAdapter


# 如果想使用管道，就必须在settings开启管道ITEM_PIPELINES
class ScrapyDangdangPipeline:
    # 在爬虫文件执行前执行的方法
    def open_spider(self, spider):
        self.fp = open('book.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):  # item就是yield后边book的对象
        # 以下这种模式不推荐，因为每传递过来一个对象，就打开一次文件，对文件的操作过于频繁
        # 注意 write方法必须要写一个字符串，而不能是其他对象
        # with open('D:\code\pythonProject\wj\json/book.json', 'a', encoding='utf-8') as fp:
        #     fp.write(str(item))
        self.fp.write(str(item))
        return item

    # 在爬虫执行完成后，执行的方法
    def close_spider(self, spider):
        self.fp.close()


# 多条管道开启,需要在settings开启管道
# 下载图片
class DangDangDownloadPipeline:
    def process_item(self, item, spider):
        url = 'http:' + item.get('src')
        filename = './books/' + item.get('name') + '.jpg'
        urllib.request.urlretrieve(url=url, filename=filename)
        return item
