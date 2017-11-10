import datetime
import re
import urllib.parse

import scrapy
from scrapy.selector import Selector
from scrapy.exceptions import DropItem


class EmagSpider(scrapy.Spider):
    name = 'emag'
    allowed_domains = ['www.emag.bg']
    search_page_url_template = 'https://www.emag.bg/search/%s'

    def __init__(self, search_term=None, *args, **kwargs):
        super(EmagSpider, self).__init__(*args, **kwargs)
        self.search_term = search_term

    def get_product_page(self, response):
        # We follow the link of the first search result, relying on a match.
        # TODO Implement name checking to verify that the item matches
        first_item = response.xpath(
            "//*[@id='products-holder']/div[@class='product-holder-grid'][1]//a/@href").extract_first()
        first_item_page = response.urljoin(first_item)
        yield scrapy.Request(first_item_page)

    def start_requests(self):
        url_escaped_search_term = urllib.parse.quote(self.search_term)
        # Emag are currently doing AB tests and the following cookie ensures we get the same version of the website
        cookies = {'ab_20': 'a'}
        yield scrapy.Request(EmagSpider.search_page_url_template % url_escaped_search_term, cookies=cookies, callback=self.get_product_page)

    def parse(self, response):
        price = Selector(response).re(r'EM\.productFullPrice = ([0-9.]+);')
        discounted_price = Selector(response).re(
            r'EM\.productDiscountedPrice = ([0-9.]+);')
        name_pattern = re.compile(
            r'EM\.product_title\s*=\s*\"(.+)\"\s*;', re.UNICODE)
        name_regex_result = Selector(text=response.text).re(name_pattern)

        if not(discounted_price or price):
            raise DropItem()

        name = ''
        if name_regex_result:
            name = name_regex_result[0].encode().decode('unicode_escape')

        yield {
            'retailer': EmagSpider.name,
            'url': response.url,
            'time': datetime.datetime.utcnow().isoformat(),
            'price': price,
            'discounted_price': discounted_price,
            'name': name
        }
