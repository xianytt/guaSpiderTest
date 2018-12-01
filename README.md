# guaSpiderTest
Test
通过scrapy框架爬取瓜子二手车所有的车辆信息。由于数据较大，所以使用分布式redisSpider进行爬取来实现Url和数据去重。
瓜子二手车有反扒策略，通过cookie进行访问。
通过xpath提取网页需要的内容
保存为字典，并存入csv。


运行方式：通过命令行scrapy crawl guazi/tenxu
