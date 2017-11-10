from scrapy.exceptions import DropItem

print('offer----------')


class PriceOfferValidationPipeline(object):

    def process_item(self, item, spider):
        if not(('discounted_price' in item and item['discounted_price']) or
               ('price' in item and item['price'])):
            raise DropItem("Missing price in %s" % item)

        return item
