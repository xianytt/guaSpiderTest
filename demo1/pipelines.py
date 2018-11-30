# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Demo1Pipeline(object):
    def process_item(self, item, spider):
        if spider.name=='tenxu':
            self.f = open('tenxu.txt', 'a', encoding='utf8')
            self.f.write(str(item)+'\n')
            self.f.close()
        return item

    def open_spider(self,spider):
        print('爬虫启动了--------')

    def close_spider(self,spider):

        print('爬虫运行结束')
class GuaZiPipeline(object):
    #处理瓜子二手车的管道
    def process_item(self, item, spider):
        if spider.name=='guazi':
            self.f = open('guazi.txt', 'a', encoding='utf8')
            self.f.write(str(item)+'\n')
            self.f.close()
        return item