import scrapy


class LdlcSpider(scrapy.Spider):
    name = "ldlc"
    allowed_domains = ["www.ldlc.com"]
    start_urls = ["https://www.ldlc.com"]

    def parse(self, response):
        pass
