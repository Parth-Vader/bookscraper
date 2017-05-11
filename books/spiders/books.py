#!/usr/bin/env python
# -*- coding: utf-8 -*-
import scrapy

class BooksSpider(scrapy.Spider):
    name = 'books'
    ratings_map = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
    }
    itemsum=0

    def start_requests(self):
        #self.pagesprev = 0
        #self.itemsprev = 0
        with open('urls.txt') as urls_file:
            for url in urls_file:
                yield scrapy.Request(url.strip())

    def parse(self, response):
        
        items = self.crawler.stats.get_value('item_scraped_count', 0)
        pages = self.crawler.stats.get_value('response_received_count', 0)
        
        f=open("AvSpeed.txt",'w')

        f.write("Average Speeds: item: '{0}' page: '{1}'".format( items*2,pages*2))

        rating = response.css('p.star-rating::attr(class)').extract_first().split(' ')[-1]
        yield {
            'rating': self.ratings_map.get(rating.lower(), ''),
            'title': response.css('.product_main h1::text').extract_first(),
            'price': response.css('.product_main p.price_color::text').re_first('£(.*)'),
            'stock': int(
                ''.join(
                    response.css('.product_main .instock.availability ::text').re('(\d+)')
                )
            ),
            'category': ''.join(
                response.css('ul.breadcrumb li:nth-last-child(2) ::text').extract()
            ).strip(),
}
