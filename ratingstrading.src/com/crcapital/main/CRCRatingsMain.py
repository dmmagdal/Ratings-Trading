"""
Property of CR Capital, LLC. All rights reserved.
Author: Cristian Gonzales
"""

import logging
from CRCRatingsWebdriver import CRCRatingsWebdriver

"""
    This is the main method that employs the use of scraping spiders and webdrivers in order to display information
    and interface with the brokerage API
"""

def main():

    # Logic for webcrawling Moody's website (use the current URL to webcrawl)
    driver = CRCRatingsWebdriver()
    moodysURL = driver.moodys()

    # Logic for webcrawling S&P's website (use the current URL to webcrawl)
    # driver = CRCRatingsWebdriver()
    # sandpURL = driver.standardandpoors()


if __name__ == "__main__":
    main()
