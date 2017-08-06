"""
    Property of CR Capital, LLC. All rights reserved.
    Author: Cristian Gonzales
"""

import logging
import scrapy

class CRCRatingsMoodys(scrapy.Spider):

    # Identifies the spider
    name = "Securities"

    # Returns iterable of Requests to begin to crawl from
    def start_requests(self):
        urls = [
            # Figure out what urls to put here...
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Handle response downloaded for each request made
    def parse(self, response):

        # Saves whole HTML page locally (temporary)
        page = response.url.split("/")[-2]
        filename = 'securities-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        logging.info('Saved file %s' % filename)