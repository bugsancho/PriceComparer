from scrapy.exceptions import DropItem


class PriceOfferValidationPipeline(object):

    def process_item(self, item, spider):
        if not(item['discounted_price'] or item['price']):
            raise DropItem("Missing price in %s" % item)
        
        return item
