from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from free_images.items import FreeImagesItem


class ImagesSpider(CrawlSpider):
    def __init__(self, *args, **kwargs):
        super(ImagesSpider, self).__init__(*args, **kwargs)
        self.category = [kwargs.get('category')]

        # Combined url to insert a category in command line.
        # Command line: scrapy crawl images -a category=category_name
        self.start_urls = [f'https://www.freeimages.com/search/{self.category}']

    name = "images"
    allowed_domains = ["freeimages.com"]
    # start_urls = ["https://www.freeimages.com/search/cat"]
    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths='//div[contains(@class, "grid-container")]'
            ),
            callback='parse',
            follow=False
        ),
    )

    def parse(self, response, **kwargs):

        item = ItemLoader(
            item=FreeImagesItem(),
            response=response,
            selector=response
        )

        item.add_xpath(
            'image_urls',
            '//div[@id="photo-wrapper"]//img[@id="photo"]/@src'
        )

        yield item.load_item()
