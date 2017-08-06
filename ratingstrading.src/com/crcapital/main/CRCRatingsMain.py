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
global logger
logger = logging.getLogger().setLevel(logging.DEBUG)

def main():

    driver = CRCRatingsWebdriver()

    moodysURL = driver.moodys()
    logger.debug("moodysURL: " + moodysURL)
    # standardAndPoorsURL = CRCRatingsWebdriver.standardandpoors()

if __name__ == "__main__":
    main()
