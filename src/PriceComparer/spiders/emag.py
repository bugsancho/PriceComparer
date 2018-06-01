import re
import json
import urllib.parse

import scrapy
from scrapy.selector import Selector

from ..product_offer import ProductOffer
from .base_spider import BaseSpider


class EmagSpider(BaseSpider):
    name = 'emag'
    allowed_domains = ['www.emag.bg']

    # def __init__(self, search_term=None, *args, **kwargs):
    #     super(EmagSpider, self).__init__(*args, **kwargs)
    #     self.search_term = search_term

    def get_search_page_url_template(self):
        return 'https://www.emag.bg/search/%s'


    # def get_product_page(self, response):
    #     # We follow the link of the first search result, relying on a match.
    #     # TODO Implement name checking to verify that the item matches the search criteria
    #     first_item = response.xpath(
    #         "//*[@id='products-holder']/div[@class='product-holder-grid'][1]//a/@href").extract_first()
    #     first_item_page = response.urljoin(first_item)
    #     yield scrapy.Request(first_item_page)

    # def start_requests(self):
    #     url_escaped_search_term = urllib.parse.quote(self.search_term)
    #     # Emag are currently doing AB tests and the following cookie ensures we get the same version of the website
    #     cookies = {'ab_20': 'a'}
    #     yield scrapy.Request(EmagSpider.search_page_url_template % url_escaped_search_term, cookies=cookies, callback=self.get_product_page)

    def parse(self, response):

        product_info_element = response.xpath('//*[@id="card_grid"]/div//button[@data-product]/@data-product').extract_first()
        product_info = json.loads(product_info_element)
        price = product_info['price']
        name = product_info['product_name']
        product_id = product_info['productid']
        # price = Selector(response).re_first(
        #     r'EM\.productFullPrice = ([0-9.]+);')
        # discounted_price = Selector(response).re_first(
        #     r'EM\.productDiscountedPrice = ([0-9.]+);')
        # name_pattern = re.compile(
        #     r'EM\.product_title\s*=\s*\"(.+)\"\s*;', re.UNICODE)
        # name_regex_result = Selector(text=response.text).re_first(name_pattern)

        # name = ''
        # if name_regex_result:
        #     # The RegEx selector returns encoded Unicode characters, so we need to decode them
        #     name = name_regex_result.encode().decode('unicode_escape')

        product_offer = ProductOffer(
            retailer=EmagSpider.name,
            url=response.url,
            name=name,
            price=price,
            product_code=product_id,
            search_id=self.search_id)

        yield product_offer
