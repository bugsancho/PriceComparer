from scrapy.exceptions import DropItem
from datetime import datetime


class PriceOfferTransformPipeline(object):

    def process_item(self, item, spider):
        if item['discounted_price']:
            item['discounted_price'] = float(item['discounted_price'])

        if item['price']:
            item['price'] = float(item['price'])

        if not item['time']:
            item['time'] = datetime.utcnow().isoformat()

        return item
