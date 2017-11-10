import scrapy
from scrapy.crawler import CrawlerProcess
from PriceComparer.spiders.emag import EmagSpider
from PriceComparer.spiders.jar import JarSpider

crawl_arguments = {'search_term': 'tp link c1200'}
process = CrawlerProcess()
process.crawl(EmagSpider, **crawl_arguments)
process.crawl(JarSpider, **crawl_arguments)
process.start()  # the script will block here until all crawling jobs are finished
