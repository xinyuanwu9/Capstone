# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BeerItem(scrapy.Item):
    # define the fields for your item here like:
    beer_rank = scrapy.Field()
    beer_name = scrapy.Field()
    beer_url = scrapy.Field()
    brewer = scrapy.Field()
    review_count = scrapy.Field()
    score = scrapy.Field()
    state = scrapy.Field()
    pass
