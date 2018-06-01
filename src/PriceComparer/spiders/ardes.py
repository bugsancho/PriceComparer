# -*- coding: utf-8 -*-
import scrapy

from urllib.parse import urljoin

from PriceComparer.spiders.base_spider import BaseSpider
from scrapy.exceptions import DropItem

from ..product_offer import ProductOffer


class ArdesSpider(BaseSpider):
    name = 'ardes'
    allowed_domains = ['ardes.bg']

    def get_search_page_url_template(self):
        return 'https://ardes.bg/products?q=%s'

    def parse(self, response):
        products_selector = response.css('.products-holder .product')
        if len(products_selector) > 0:
            first_product_selector = products_selector[0]
        else:
            raise DropItem("Could not find search result")
        
        product_id = first_product_selector.xpath('./@id').extract_first()
        url = first_product_selector.css('a::attr(href)').extract_first()
        absolute_url = urljoin(response.url, url)
        name = first_product_selector.css('.title > a > span').xpath('./text()').extract_first()

        price_parts = first_product_selector.css('.price-num').xpath('.//text()').extract()[:2]
        price = '.'.join(price_parts)
        
        product_offer = ProductOffer(
            retailer=ArdesSpider.name,
            url=absolute_url,
            name=name,
            price=price,
            product_code=product_id,
            search_id=self.search_id)

        yield product_offer
