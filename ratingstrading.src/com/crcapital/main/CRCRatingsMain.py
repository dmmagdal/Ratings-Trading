"""
Property of CR Capital, LLC. All rights reserved.
Author: Cristian Gonzales
"""

import logging

import sys
sys.path.append('/com/crcapital/ratingscrawler/ratingscrawler')

# Scrapy API
from scrapy.crawler import CrawlerProcess


"""
    This is the main method that employs the use of scraping spiders and webdrivers in order to display information
    and interface with the brokerage API. The logic behind implementing Selenium is to have a more robust way of
    the URL after all the filters are selected. In the case that there are minute changes in the structure of the
    webpage or URL, it will be less prone to bugs.
"""

def main():

    # Crawler process
    process = CrawlerProcess({'SPIDER_MODULES': 'com.crcapital.ratingscrawler.ratingscrawler.spiders'})

    process.crawl("Securities")
    process.start()


if __name__ == "__main__":
    main()