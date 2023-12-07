# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import pymysql
from caipiao.settings import MYSQL


class TupianzjPipeline:
    # 开始执行
    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host=MYSQL['host'],
            port=MYSQL['port'],
            user=MYSQL['user'],
            password=MYSQL['password'],
            database=MYSQL['database']
        )

    # 结束执行
    def close_spider(self, spider):
        if self.conn:
            self.conn.close()

    def process_item(self, item, spider):
        try:
            cursor = self.conn.cursor()
            sql = "insert into tu (name, img_src,local_path) values (%s, %s,%s)"
            cursor.execute(sql, (item['name'], item['img_src'], item['local_path']))
            self.conn.commit()
        except Exception as e:  # 捕获异常并打印错误信息
            print(f"Error: {e}")
            self.conn.rollback()
        finally:
            if cursor:
                cursor.close()
        return item


# 想要使用ImagesPipeline,必须单独设置一个配置，用来保存文件的文件夹
# 利用图片管道帮我们完成数据下载操作
class MeinvSavePipeline(ImagesPipeline):
    # 负责下载
    def get_media_requests(self, item, info):
        return scrapy.Request(item['img_src'])

    # 文件路径
    def file_pass(self, request, info=None):
        file_name = request.url.split("/")[-1]
        return f"img/{file_name}"

    # 返回文件详细信息
    def file_completed(self, results, item, info):
        ok, finfo = results[0]
        item['local_path'] = finfo["path"]
        return item
