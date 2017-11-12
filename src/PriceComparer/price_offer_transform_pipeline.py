from datetime import datetime


class PriceOfferTransformPipeline(object):

    def process_item(self, item, spider):

        if item['price']:
            item['price'] = float(item['price'])

        # Optional attributes
        if 'discounted_price' in item and item['discounted_price']:
            item['discounted_price'] = float(item['discounted_price'])

        if not ('time' in item and item['time']):
            item['time'] = datetime.utcnow().isoformat()

        return item
