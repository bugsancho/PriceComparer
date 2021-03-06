# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductOffer(scrapy.Item):
    retailer = scrapy.Field()
    url = scrapy.Field()
    time = scrapy.Field()
    price = scrapy.Field()
    discounted_price = scrapy.Field()
    name = scrapy.Field()
    product_code = scrapy.Field()
    search_id = scrapy.Field()
