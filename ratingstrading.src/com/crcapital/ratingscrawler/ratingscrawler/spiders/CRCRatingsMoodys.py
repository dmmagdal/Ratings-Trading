"""
    Property of CR Capital, LLC. All rights reserved.
    Author: Cristian Gonzales
"""

import logging
import scrapy

from com.crcapital.main import CRCRatingsWebdriver
from com.crcapital.ratingscrawler.ratingscrawler.CRCRatingsPair import CRCRatingsPair

# TODO: Incorporate error handling so that if the URL returned is an error then it can be handled appropriately

class CRCRatingsMoodys(scrapy.Spider):

    # Identifies the spider
    name = "Securities"

    # Initialize key-value pair as an empty list
    global pairsList
    pairsList = []

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
        # Declaring the names, statuses, and titles lists
        names = response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "mdcResearchDocLink", " " ))]'
        ).extract()
        statuses = response.css(
            '.mdcResearchDocTypeValue~ td+ td a'
        ).extract()
        titles = len(response.xpath(
                '//*[contains(concat( " ", @class, " " ), concat( " ", "mdcResearchDocLink", " " ))]'
        ))
        # Declaring the pair object to add to the global list of key-value pairs
        pairObj = CRCRatingsPair
        for title in range(titles):
            # Setting the names
            pairObj.set_name(names[title])
            logging.debug(pairObj.get_name())
            # Setting the status
            pairObj.set_status(statuses[title])
            logging.debug(pairObj.get_status())
            # Adding the obj to the list
            pairsList.append(pairObj)