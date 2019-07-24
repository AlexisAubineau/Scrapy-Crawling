# -*- coding: utf-8 -*-
import scrapy


class ProfileGithubSpider(scrapy.Spider):
    name = 'profile_github'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/Alexis-Gucci/']

    def parse(self, response):
        profiles = response.xpath("//main[@id='js-pjax-container']")
        for profile in profiles:

            image = profile.xpath(".//a[contains(@class, 'u-photo')]//@src").extract()
            status = profile.xpath(".//div[contains(@class, 'user-status-container')]//div[contains(@class, 'user-status-message-wrapper')]//div/text()").extract_first()
            yield {'image': image, 'status': status}

            name = profile.xpath(".//h1[@class='vcard-names']//span[contains(@class, 'p-name')]/text()").extract()
            nickname = profile.xpath(".//h1[@class='vcard-names']//span[contains(@class, 'p-nickname')]/text()").extract()
            bio = profile.xpath(".//div[contains(@class, 'd-none')]//div[contains(@class, 'p-note')]//div/text()").extract()
            works = profile.xpath(".//div[contains(@class, 'd-none')]//li[contains(@itemprop, 'worksFor')]//div/text()").extract_first()
            location = profile.xpath(".//div[contains(@class, 'd-none')]//li[contains(@itemprop, 'homeLocation')]//span/text()").extract_first()
            url = profile.xpath(".//div[contains(@class, 'd-none')]//li[contains(@itemprop, 'url')]//a/text()").extract_first()

            yield{'name': name, 'nickname': nickname, 'bio': bio, 'works': works, 'location': location, 'url': url}
