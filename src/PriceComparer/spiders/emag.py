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


    def get_search_page_url_template(self):
        return 'https://www.emag.bg/search/%s'


    def parse(self, response):

        product_info_element = response.xpath('//*[@id="card_grid"]/div//button[@data-product]/@data-product').extract_first()
        product_info = json.loads(product_info_element)
        price = product_info['price']
        name = product_info['product_name']
        product_id = product_info['productid']

        product_url = response.css('.js-product-url::attr(href)').extract_first()

        product_offer = ProductOffer(
            retailer=EmagSpider.name,
            url=product_url,
            name=name,
            price=price,
            product_code=product_id,
            search_id=self.search_id)

        yield product_offer
