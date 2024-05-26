import scrapy


class ImagesSpider(scrapy.Spider):
    name = "images"
    allowed_domains = ["freeimages.com"]
    start_urls = ["https://freeimages.com"]

    def parse(self, response, **kwargs):
        pass
