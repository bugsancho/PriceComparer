import scrapy
import urllib


class BaseSpider(scrapy.Spider):
    search_page_url_template = 'https://www.pcstore.bg/bg/catalogsearch/result/?q=%s'

    def __init__(self, search_term=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.search_term = search_term

    def start_requests(self):
        url_escaped_search_term = urllib.parse.quote(self.search_term)
        yield scrapy.Request(self.get_search_page_url_template() % url_escaped_search_term)

    def get_search_page_url_template(self):
        raise NotImplementedError
