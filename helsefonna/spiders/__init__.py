# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.


from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.item import Item, Field
import scrapy

#klasser, ligner på funksjon og dataobjekt
class Items(Item):
  referer = Field() 
  response = Field()
  status = Field()
  #samme egenskaper som field, kan ta imot issubclass

class MySpider(CrawlSpider):
  name = "torstein-test"
  target_domains = ["torstein.io"]
  start_urls = ["https://torstein.io/"]
  #handle_httpstatus_list = [404,200]
  custom_settings = {'CONCURRENT_REQUESTS': 2,'DOWNLOAD_DELAY': 0.5, 'FEED_URI': "404.csv", 'FEED_FORMAT': "csv"}
  rules = (
    Rule(
      LinkExtractor(allow_domains=target_domains),
      callback="",
      follow = True
      ),
      Rule(
        LinkExtractor(allow_domains=("")),
        callback="",
        follow = False
      )

  )

  def parse_item(self, response):
    item = scrapy.Item()
    item["referer"]=response.request.headers.get("Referer", None)
    item["response"]=response.url
    self.logger.info("RRR.url")
    yield item
    
    
  





 

