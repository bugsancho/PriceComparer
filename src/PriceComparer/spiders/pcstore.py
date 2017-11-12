import scrapy
import urllib
from ..product_offer import ProductOffer


class PcstoreSpider(scrapy.Spider):
    name = 'pcstore'
    allowed_domains = ['pcstore.bg']
    search_page_url_template = 'https://www.pcstore.bg/bg/catalogsearch/result/?q=%s'

    def __init__(self, search_term=None, *args, **kwargs):
        super(PcstoreSpider, self).__init__(*args, **kwargs)
        self.search_term = search_term

    def start_requests(self):
        url_escaped_search_term = urllib.parse.quote(self.search_term)
        yield scrapy.Request(PcstoreSpider.search_page_url_template % url_escaped_search_term)

    def parse(self, response):
        product_container = response.css('.products-grid .item.first')

        product_name = product_container.css(
            '.product-name > a::attr(title)').extract_first()
        url = product_container.css(
            '.product-name > a::attr(href)').extract_first()

        discounted_price_parts = product_container.css(
            '.price-box .special-price .price').xpath('.//text()').extract()[:2]
        discounted_price = ''.join(discounted_price_parts)

        original_price_parts = product_container.css(
            '.price-box .old-price .price').xpath('.//text()').extract()[:2]
        original_price = ''.join(original_price_parts)

        regular_price_parts = product_container.css(
            '.price-box .regular-price .price').xpath('.//text()').extract()[:2]
        regular_price = ''.join(regular_price_parts)

        product_offer = ProductOffer(
            retailer="pcstore",
            url=url,
            name=product_name,
            price=original_price or regular_price,
            discounted_price=discounted_price or None)

        yield product_offer
