# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import Demo1Item

from scrapy_redis.spiders import RedisCrawlSpider


class TenxuSpider(RedisCrawlSpider):
    name = 'tenxu'
    allowed_domains = ['tencent.com']
    # start_urls = ['https://hr.tencent.com/position.php?']
    redis_key = 'tenxu'

    rules = (
        Rule(LinkExtractor(allow=r'&start=\d+#a',), follow=True),
        Rule(LinkExtractor(allow=r'id=\d+&keywords=&tid=0&lid=0'), callback='parse_item2',
             follow=False),
    )

    def parse_item2(self, response):
        # 提取职位页面的数据
        table = response.xpath('//table[@class="tablelist textl"]')
        name = response.xpath('//td[@id="sharetitle"]/text()').get()
        address = table.xpath('./tr[2]/td[1]/text()').get()
        group = table.xpath('./tr[2]/td[2]/text()').get()
        number = table.xpath('./tr[2]/td[3]/text()').get()
        work = table.xpath('./tr[3]//ul/li/text()').getall()
        item = Demo1Item(
            name=name,
            address=address,
            group=group,
            number=number,
            work=work,
        )
        # 交给管道处理解析后的数据
        yield item
