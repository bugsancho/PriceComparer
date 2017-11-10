import scrapy
import urllib.parse
import re
from scrapy.selector import Selector

class EmagSpider(scrapy.Spider):
    name = 'emag'
    allowed_domains = ['www.emag.bg']

    def __init__(self, search_term=None, *args, **kwargs):
        super(EmagSpider, self).__init__(*args, **kwargs)
        self.search_term = search_term

    def get_product_page(self, response):
        first_item = response.xpath("//*[@id='products-holder']/div[@class='product-holder-grid'][1]//a/@href").extract_first()
        first_item_page = response.urljoin(first_item)
        yield scrapy.Request(first_item_page, callback=self.parse_product_page)

    def start_requests(self):
        yield scrapy.Request('https://www.emag.bg/search/%s' % urllib.parse.quote(self.search_term),cookies={'ab_20': 'a'}, callback=self.get_product_page)
        

   

    def parse_product_page(self, response):    
        price = Selector(response).re('EM\.productFullPrice = ([0-9.]+);')
        discounted_price = Selector(response).re('EM\.productDiscountedPrice = ([0-9.]+);')
        name_pattern = re.compile('EM\.product_title\s*=\s*\"(.+)\"\s*;', re.UNICODE)
        name_regex_result = Selector(text=response.text).re(name_pattern)
        name = ''
        if name_regex_result and len(name_regex_result) > 0:
            name = name_regex_result[0].encode().decode('unicode_escape')

        print(price)
        yield {
            'price': price,
            'discounted_price' : discounted_price,
            'name': name
        }
