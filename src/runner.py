import uuid

from scrapy.crawler import CrawlerProcess
from scrapy.spiderloader import SpiderLoader
from scrapy.utils.project import get_project_settings

from PriceComparer.persistance.database import ensure_database_exists

project_settings = get_project_settings()
loader = SpiderLoader(project_settings)
process = CrawlerProcess(project_settings)

spiders = loader.list()
crawl_arguments = {'search_term': 'huawei p10',
                   'search_id': str(uuid.uuid4())}

ensure_database_exists()
for spider in spiders:
    process.crawl(spider, **crawl_arguments)
process.start()  # the script will block here until all crawling jobs are finished
