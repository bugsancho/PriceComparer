import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from PriceComparer.spiders.emag import EmagSpider
from PriceComparer.spiders.jar import JarSpider
from PriceComparer.spiders.pcstore import PcstoreSpider

crawl_arguments = {'search_term': 'tp link wr840n'}
process = CrawlerProcess(get_project_settings())
process.crawl(EmagSpider, **crawl_arguments)
process.crawl(JarSpider, **crawl_arguments)
process.crawl(PcstoreSpider, **crawl_arguments)
process.start()  # the script will block here until all crawling jobs are finished
