# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DuitangComItem(scrapy.Item):
    # define the fields for your item here like:
    TextContent = scrapy.Field()
    Link = scrapy.Field()


class ImgsproItem(scrapy.Item):
    # define the fields for your item here like:
    path = scrapy.Field()
    img_src = scrapy.Field()
