import scrapy


class LazadaSpider(scrapy.Spider):
    name = 'lazada'
    allowed_domains = ['lazada.vn']
    start_urls = ['http://lazada.vn/']

    def parse(self, response):
        pass
