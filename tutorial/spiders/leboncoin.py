# -*- coding: utf-8 -*-
import scrapy
import json
from tutorial.items import TutorialItem

class LeboncoinSpider(scrapy.Spider):
    name = 'leboncoin'
    allowed_domains = ['leboncoin.fr']
    start_urls = ['http://leboncoin.fr/annonces/offres/aquitaine/']

    frmdata = {"limit": 35, "limit_alu": 3, "offset": 0, "filters": {"category": {}, "enums": {"ad_type": ["offer"]}, "location": {
        "locations": [{"locationType": "region", "label": "Aquitaine", "region_id": "2"}]}, "keywords": {},
                                                        "ranges": {}}}
    headr = {"api_key": "ba0c2dad52b3ec"}
    url = "https://api.leboncoin.fr/finder/search"
    i = 1

    def start_requests(self):
        yield scrapy.Request(self.url, callback=self.parse, method='POST', body=json.dumps(self.frmdata), headers=self.headr)

    def parse(self, response):
        jsonresponse = json.loads(response.text)
        for ads in jsonresponse["ads"]:
            item = TutorialItem()
            if "subject" in ads:
                item["subject"] = ads["subject"]
            if "price" in ads:
                item["price"] = ads["price"][0]
            if "category_name" in ads:
                item["category"] = ads["category_name"]
            if "location" in ads:
                if "city" in ads["location"]:
                    item["location"] = ads["location"]["city"]
            item["url"] = ads["url"]
            yield {'object': item}
        self.i = self.i + 1
        print(self.i)

        if len(jsonresponse["ads"]) == 35:
            self.frmdata["offset"] = self.frmdata["offset"] + 35
            yield scrapy.Request(self.url, callback=self.parse, method='POST', body=json.dumps(self.frmdata), headers=self.headr, dont_filter=True)




