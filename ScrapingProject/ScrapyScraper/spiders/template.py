import scrapy


class TemplateSpider(scrapy.Spider):
    name = "template"
    allowed_domains = ["www.google.com"]
    start_urls = ["https://www.google.com"]

    def parse(self, response):
        pass
