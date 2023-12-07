# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from caipiao.settings import MYSQL
import pymongo
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

"""
存储数据方案：
    1.数据要存储在csv文件中
    2.数据存储在mysql数据库中
    3.数据存储在mongodb数据库中
    4.文件的存储

"""


class CaipiaoPipeline:
    # 开始执行
    def open_spider(self, spider):
        self.f = open("./双色球.csv", mode="a", encoding="utf-8")

    def process_item(self, item, spider):
        self.f.write(f"{item['qihao']},{'_'.join(item['red_ball'])},{item['blue_ball']}\n")
        return item

    # 结束执行
    def close_spider(self, spider):
        if self.f:
            self.f.close()



class CaipiaoMySQLPipeline:
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
            sql = "insert into caipiao (qihao, red_ball, blue_ball) values (%s, %s, %s)"
            cursor.execute(sql, (item['qihao'], '_'.join(item['red_ball']), item['blue_ball']))
            self.conn.commit()
        except Exception as e:  # 捕获异常并打印错误信息
            print(f"Error: {e}")
            self.conn.rollback()
        finally:
            if cursor:
                cursor.close()
        return item


class CaipiaoMongoDBPipeline:
    # 开始执行
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host="localhost", port=27017)
        db = self.client['python']
        self.collection = db['caipiao']

    # 结束执行
    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.collection.insert_one({"qihao": item['qihao'], "red_ball": item['red_ball'], "blue_ball": item['blue_ball']})
        return item
