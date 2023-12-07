# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# 定义数据格式
class CaipiaoItem(scrapy.Item):
    # define the fields for your item here like:
    qihao = scrapy.Field()
    red_ball = scrapy.Field()
    blue_ball = scrapy.Field()