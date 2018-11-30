# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Demo1Item(scrapy.Item):
    '''腾讯爬虫数据的模型类'''
    name = scrapy.Field()
    group = scrapy.Field()
    number = scrapy.Field()
    address = scrapy.Field()
    work = scrapy.Field()


class GuziItem(scrapy.Item):

    '''瓜子二手车爬虫数据模型类'''
    #车量信息：
    vehicle_info= scrapy.Field()
    #上牌时间：
    ttime=scrapy.Field()
    #地区：
    addr=scrapy.Field()
    #价格：
    price=scrapy.Field()
   # 里程：
    mileage=scrapy.Field()