# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    subject = scrapy.Field()
    price = scrapy.Field()
    category = scrapy.Field()
    location = scrapy.Field()
    url = scrapy.Field()
