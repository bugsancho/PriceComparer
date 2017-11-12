import scrapy


class PcstoreSpider(scrapy.Spider):
    name = 'pcstore'
    allowed_domains = ['pcstore.bg']
    start_urls = ['https://www.pcstore.bg/']

    def parse(self, response):
        pass
