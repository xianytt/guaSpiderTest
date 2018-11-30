# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import GuziItem

class GuaziSpider(CrawlSpider):
    name = 'guazi'
    allowed_domains = ['guazi.com']
    start_urls = ['https://www.guazi.com/cs/buy']

    rules = (
        #所有城市的连接提取出来
        # Rule(LinkExtractor(restrict_xpaths='//div[@class="city-box-parent"]'), follow=False),
        #提取每个页面的url地址
        Rule(LinkExtractor(restrict_xpaths='//ul[@class="pageLink clearfix"]'), follow=True),
        #提取每辆车的url地址
        Rule(LinkExtractor(restrict_xpaths='//ul[@class ="carlist clearfix js-top"]'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        #提取车辆描述信息
        vehicle_info=response.xpath('//h2[@class="titlebox"]/text()').get().strip()
        #获取上牌时间
        ttime = response.xpath('//ul[@class="assort clearfix"]/li[1]/span/text()').get().strip()
        #地区：
        addr=response.xpath('//ul[@class="assort clearfix"]/li[3]/span/text()').get().strip()
        #里程：
        mileage=response.xpath('//ul[@class="assort clearfix"]/li[2]/span/text()').get().strip()
        #价格：
        price=response.xpath('//div[@class="pricebox js-disprice"]/span[1]/text()').get().strip()
        item = GuziItem(
            vehicle_info=vehicle_info,
            ttime=ttime,
            addr=addr,
            mileage=mileage,
            price=price
        )
        yield item