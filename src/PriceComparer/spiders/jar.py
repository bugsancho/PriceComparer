import scrapy


class JarSpider(scrapy.Spider):
    name = 'jar'
    allowed_domains = ['www.jarcomputers.com']
    start_urls = ['http://www.jarcomputers.com/']

    def parse(self, response):
        pass
