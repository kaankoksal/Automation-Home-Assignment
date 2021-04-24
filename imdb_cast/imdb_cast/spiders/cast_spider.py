import scrapy
from ..items import ImdbCastItem

class CastSpider(scrapy.Spider):
    name = 'cast_spider'
    start_urls = ['https://www.imdb.com/chart/top/']

    def parse(self, response):
        # GET URLS FOR EACH MOVIE TITLE
        #    extract the /title/.../ strings
        urls = response.css("td.titleColumn a::attr(href)").extract() 
        for url in urls:
            # combine Response's url with possible relative url
            request = scrapy.Request(response.urljoin(url), callback=self.parseCast) 
            yield request
        

    def parseCast(self, response):
        # SCRAPE CAST MEMBERS FROM EACH CAST LIST
        cast_list = response.css("td.primary_photo a img::attr(title)").extract()     
        for member in cast_list:
            cast = ImdbCastItem()
            cast['name'] = str(member).strip()
            yield cast