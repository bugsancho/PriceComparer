import urllib.parse

import scrapy

from ..product_offer import ProductOffer


class JarSpider(scrapy.Spider):
    name = 'jar'
    allowed_domains = ['www.jarcomputers.com']
    search_page_url_template = 'https://www.jarcomputers.com/search?q=%s'

    def __init__(self, search_term=None, *args, **kwargs):
        super(JarSpider, self).__init__(*args, **kwargs)
        self.search_term = search_term

    def start_requests(self):
        url_escaped_search_term = urllib.parse.quote(self.search_term)
        yield scrapy.Request(JarSpider.search_page_url_template % url_escaped_search_term)

    def parse(self, response):
        first_product_selector = response.selector.xpath(
            '//*[@id="product_list"]/li[1]')
        product_url = first_product_selector.css(
            '.plttl::attr(href)').extract_first()
        product_name = first_product_selector.css(
            '.plttl::attr(title)').extract_first()
        product_code = first_product_selector.css(
            '[name=code]::attr(value)').extract_first()
        price_integer_part = first_product_selector.xpath(
            './/*[@class="price"]/div/text()').extract_first()
        price_decimal_part = first_product_selector.xpath(
            './/*[@class="price2"]/text()').extract_first()

        combined_price = None
        if price_decimal_part and price_integer_part:
            price_decimal_part = price_decimal_part.replace(' лв', '')
            combined_price = price_integer_part + price_decimal_part

        product_offer = ProductOffer(
            retailer="jar",
            url=product_url,
            name=product_name,
            price=combined_price,
            product_code=product_code)

        yield product_offer
