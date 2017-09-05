"""
    Property of CR Capital, LLC. All rights reserved.
    Author: Cristian Gonzales
"""

import logging

import scrapy

import threading
from bs4 import BeautifulSoup

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

    """
        Handle response downloaded for each request made
        :param response: response from Scrapy scraping
        :return: void
    """
    def parse(self, response):
        try:
            # Declaring the names, statuses, and titles lists
            comp_names = response.xpath(
                '//*[contains(concat( " ", @class, " " ), concat( " ", "mdcResearchDocLink", " " ))]'
            ).extract()
            logging.debug("names length: " + str(len(comp_names)))

            # Commented out because it was inconsistent with the length of the names array
            # credit_statuses = response.css(
            #     '.mdcResearchDocTypeValue~ td+ td a'
            # ).extract()
            credit_statuses = response.css(
                '.mdcResearchDocTypeValue~ td+ td'
            ).extract()
            logging.debug("statuses length: " + str(len(credit_statuses)))

            # Start a new thread to actually parse the data
            threading.Thread(target=self.data_storing(comp_names, credit_statuses)).start()
        except Exception as e:
            logging.error(e)

    """
        New thread to parse the data as HTML and store inside ADT
        :param names: The names as HTML from Scrapy webscraping
        :param statuses: The statuses as HTML from Scrapy webscraping
        :return: void
    """
    def data_storing(self, names, statuses):
        # Declaring the pair object to add to the global list of key-value pairs
        pairObj = CRCRatingsPair()

        # Storing each item in ADT (to be stored in an array of ADTs)
        for i in range(len(names)):
            try:
                # logging.debug("Company name (HTML): " + names[i])
                # logging.debug("Credit status (HTML): " + statuses[i])

                # Setting the names using BeautifulSoup
                name_soup = BeautifulSoup(names[i], "lxml")
                name = name_soup.a.string
                logging.debug(name)
                pairObj.set_name(name)
                logging.debug("ADT name: " + pairObj.get_name())

                # Setting the status using BeautifulSoup
                status_soup = BeautifulSoup(statuses[i], "lxml")
                status = status_soup.a.string
                logging.debug(status)
                pairObj.set_status(status)
                logging.debug("ADT status: " + pairObj.get_status())

                # Quick hack around ellipses is to just skip it for simplicity. This is something that can be
                # explored in the future. For now, if the name contains an ellipses, then the object it is
                # associated with is not added to the list.
                if "..." not in name:
                    # Adding the obj to the list
                    self.pairsList.append(pairObj)
            except Exception as e:
                logging.error(e)