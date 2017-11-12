from ..product_offer import ProductOffer
from .base_spider import BaseSpider


class TechnomarketSpider(BaseSpider):
    name = 'technomarket'
    allowed_domains = ['www.technomarket.bg']

    def get_search_page_url_template(self):
        return 'https://www.technomarket.bg/search/?query=%s'

    def parse(self, response):
        product_container = response.xpath(
            '//*[@id="contentholder"]/section/div/div[3]/div[1]')

        relative_url = product_container.xpath(
            './/*[@itemprop="url"]/@href').extract_first()
        absolute_url = response.urljoin(relative_url)

        product_name = product_container.xpath(
            './/*[@itemprop="name"]/text()').extract_first()

        product_code = product_container.xpath(
            './/*[@itemprop="productID"]/text()').extract_first()

        price_parts = product_container.xpath(
            './/*[@itemprop="price"]//text()').extract()[:2]
        price = ''.join(price_parts) if price_parts else None

        product_offer = ProductOffer(
            retailer="technomarket",
            url=absolute_url,
            name=product_name,
            product_code=product_code,
            price=price)

        yield product_offer
