# -*- coding: utf-8 -*-

import re
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "general"
    allowed_domains = ["ipn.ge"]
    start_urls = (
        'http://ipn.ge/',
    )
    
    def valid_word(self, word):
        pattern = '^[ა-ზ]*$'
        return re.match(pattern, word)
    
    def save_word(self, word):
        if word and self.valid_word(word):
            print word

    def split_text(self, texts):
        for text in texts:
            words = re.split(r'\s|[.,!?":;]', text.encode('utf-8'))
            for word in words:
                self.save_word(word)

    def parse(self, response):
        texts = response.xpath(".//text()").extract()
        self.split_text(texts)


