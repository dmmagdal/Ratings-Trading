"""
    Property of CR Capital, LLC. All rights reserved.
    Author: Cristian Gonzales
"""

import scrapy

from com.crcapital.webdriver import CRCRatingsWebdriver


# TODO: Incorporate error handling so that if the URL returned is an error then it can be handled appropriately
class CRCRatingsMoodys(scrapy.Spider):

    # Identifies the spider
    name = "EDGARSEC"

    # Returns iterable of Requests to begin to crawl from
    def start_requests(self):
        # Logic for webcrawling Moody's website (use the current URL to webcrawl)
        driver = CRCRatingsWebdriver.CRCRatingsWebdriver()
        edgarSEC = driver.edgarSEC()
        # Array of URLs to iterate over
        urls = [
            edgarSEC
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Handle response downloaded for each request made
    def parse(self, response):
        # Determine if there are filings for the security entered
        yield
        {

        }