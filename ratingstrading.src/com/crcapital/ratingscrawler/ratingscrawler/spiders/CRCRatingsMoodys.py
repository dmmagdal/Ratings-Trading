"""
    Property of CR Capital, LLC. All rights reserved.
    Author: Cristian Gonzales
"""

import logging
import scrapy

from com.crcapital.main import CRCRatingsWebdriver

# TODO: Incorporate error handling so that if the URL returned is an error then it can be handled appropriately
class CRCRatingsMoodys(scrapy.Spider):

    # Identifies the spider
    name = "Securities"

    # Returns iterable of Requests to begin to crawl from
    def start_requests(self):
        # Logic for webcrawling Moody's website (use the current URL to webcrawl)
        driver = CRCRatingsWebdriver.CRCRatingsWebdriver()
        moodysURL = driver.moodys()
        # Array of URLs to iterate over
        urls = [
            moodysURL
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Handle response downloaded for each request made
    def parse(self, response):
        # For each title...
        for title in response.xpath(
                '//*[contains(concat( " ", @class, " " ), concat( " ", "mdcResearchDocLink", " " ))]'
        ):
            # Dictionary of titles to determine which are publicly traded or not...
            yield
            {
                'TITLE': response.xpath(
                    '//*[contains(concat( " ", @class, " " ), concat( " ", "mdcResearchDocLink", " " ))]'
                ).extract(),
                'COMPANY': response.css(
                    '.mdcResearchDocTypeValue~ td+ td a'
                ).extract()
            }