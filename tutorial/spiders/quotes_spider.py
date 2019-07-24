# -*- coding: utf-8 -*-
import scrapy


class QuotesSpiderSpider(scrapy.Spider):
    name = 'quotes_spider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/page/3/']

    def parse(self, response):
        quotes = response.xpath("//div[@class='quote']")
        for quote in quotes:
            text = quote.xpath(".//span[@class='text']/text()").extract_first()
            author = quote.xpath(".//small/text()").extract_first()
            tags = quote.xpath(".//div[@class='tags']//a[@class='tag']/text()").extract()
            more = quote.xpath(".//span/a/@href").extract_first()
            yield{'quote': text, "author": author, "tags": tags, "more": more}
