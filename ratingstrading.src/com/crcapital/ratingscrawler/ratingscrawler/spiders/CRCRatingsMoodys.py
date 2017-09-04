"""
    Property of CR Capital, LLC. All rights reserved.
    Author: Cristian Gonzales
"""

import logging

import scrapy

import threading

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
        comp_names = response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "mdcResearchDocLink", " " ))]'
        ).extract()
        logging.debug("names length: " + str(len(comp_names)))

        # Commented out because it was inconsistent with the length of the names array
        # statuses = response.css(
        #     '.mdcResearchDocTypeValue~ td+ td a'
        # ).extract()
        credit_statuses = response.css(
            '.mdcResearchDocTypeValue~ td+ td'
        ).extract()
        logging.debug("statuses length: " + str(len(credit_statuses)))

        # Start a new thread to actually parse the data
        threading.Thread(target=self.data_storing(comp_names, credit_statuses)).start()

    def data_storing(self, names, statuses):
        # Declaring the pair object to add to the global list of key-value pairs
        pairObj = CRCRatingsPair()

        for i in range(len(names)):
            try:
                # Debugging
                logging.debug("Company name: " + names[i])
                logging.debug("Credit status: " + statuses[i])
                # Setting the names
                pairObj.set_name(names[i])
                logging.debug("ADT name: " + pairObj.get_name())
                # Setting the status
                pairObj.set_status(statuses[i])
                logging.debug("ADT status: " + pairObj.get_status())
                # Adding the obj to the list
                pairsList.append(pairObj)
            except Exception as e:
                logging.error(e)