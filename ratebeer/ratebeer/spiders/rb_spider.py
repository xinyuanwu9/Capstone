import scrapy
from ratebeer.items import BeerItem
from scrapy import Selector

class RateBeerSpider(scrapy.Spider):
    name = "ratebeer_spider"
    allowed_domains = ["http://www.ratebeer.com/"]
    def start_requests(self):
        start_url = "https://www.ratebeer.com/BestInMyArea.asp?CountryID=213&StateID="
        urls = [start_url + str(i) for i in range(1, 6)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = BeerItem()
        beer_table = response.xpath('//*[@id="rbbody"]/div[3]/div[2]/table[2]').extract()
        for i in range(2, 27):
            # beer_row = Selector(text=beer_table[0]).xpath('//tr[i]').extract()
            # for j in range(1, 6):
            try:
                beer_rank = Selector(text=beer_table[0]).xpath('//*/tr['+str(i)+']/td[1]/text()').extract()[0]
            except:
                beer_rank = None
            item['beer_rank'] = beer_rank

            try:
                beer_name = \
                    Selector(text=beer_table[0]).xpath('//*/tr['+str(i)+']/td[2]//*/text()').extract()[0].encode('utf-8')
            except:
                beer_name = None
            item['beer_name'] = beer_name

            try:
                brewer = Selector(text=beer_table[0]).xpath('//*/tr['+str(i)+']/td[3]//*/text()').extract()[0]
            except:
                brewer = None
            item['brewer'] = brewer

            try:
                review_count = Selector(text=beer_table[0]).xpath('//*/tr['+str(i)+']/td[4]/text()').extract()[0]
            except:
                review_count = None
            item['review_count'] = review_count

            try:
                score = Selector(text=beer_table[0]).xpath('//*/tr['+str(i)+']/td[5]//*/text()').extract()[0]
            except:
                score = None
            item['score'] = score

            # try:
            # beer_url = Selector(text=beer_table[0]).xpath('//tr[i]/td[j]/text()').extract()[0]
            # except:
            #     beer_url = None
            # item['beer_url'] = beer_url
            # request = scrapy.Request(url=beer_url, callback=self.parse_beer_product)
            print "*" * 50
            print beer_rank, beer_name, brewer, review_count, score
            print "*" * 50

            yield item
    # def parse_beer_product(self, response):





