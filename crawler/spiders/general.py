# -*- coding: utf-8 -*-

import re
import scrapy
from urlparse import urlparse
from urlparse import urljoin
from scrapy import Request
class ExampleSpider(scrapy.Spider):
    name = "general"
    allowed_domains = ["ipn.ge", "www.interpressnews.ge"]
    start_urls = (
        'http://ipn.ge/',
    )

    def isHref(self, href):
        blacklist = ["/", "#", "javascript:void(0)"]
        if href in blacklist:
            return False
        if href.startswith("#"):
            return False
        if href.startswith("javascript:"):
            return False
        return True

    def isInternal(self, href_parts, host):
        host_part = href_parts[1]
        if host_part and host not in host_part and host_part not in host:
            return False
        return True

    def isHttp(self, href_parts):
        scheme_part = href_parts[0]
        if scheme_part:
            if scheme_part in ["http", "https"]:
                return True
            else:
                return False
        else:
            return True



    def valid_word(self, word):
        pattern = '^[ა-ჰ,\-]*$'
        return re.match(pattern, word)
    
    def save_word(self, word):
        if word and self.valid_word(word):
            print word

    def split_text(self, texts):
        for text in texts:
            words = re.split(r'\s|[.,!?":;]', text.encode('utf-8'))
            for word in words:
                self.save_word(word)

    urls = []


    def parse(self, response):
        print response.url
        texts = response.xpath(".//text()").extract()
        if texts:
            self.split_text(texts)
        hrefs = response.xpath(".//a/@href").extract()
        if hrefs:
            for href in hrefs:
                href_parts = urlparse(href)
                if not self.isHref(href):
                    continue
                if not self.isHttp(href_parts):
                    continue
                if not self.isInternal(href_parts, urlparse(response.url)[1]):
                    continue
                if not href_parts[0] and not href_parts[1]:
                    href = urljoin(response.url, href) 
                if href not in self.urls:
                    self.urls.append(href)
            for url in self.urls:
                print url
                yield scrapy.Request(url, callback=lambda response: self.parse(response))

