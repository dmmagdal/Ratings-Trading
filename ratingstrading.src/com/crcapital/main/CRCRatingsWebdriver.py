"""
    Property of CR Capital, LLC. All rights reserved.
    Author: Cristian Gonzales
"""

import logging

from selenium import webdriver
from selenium.webdriver import ActionChains

"""
    Webdriver used to navigate the respective credit ratings website (Moodys or S&P) and return the url of the
    webpage that needs to be scraped.

    :var myDriver: The global driver to navigate through the respective webpage (Moody's/S&P)
"""

# driver = None

class CRCRatingsWebdriver:
    global logger, driver
    logger = logging.getLogger().setLevel(logging.DEBUG)

    """
        Constructor defining webdriver
        NOTE: User must have one of the following webdrivers installed:
        – Chrome (https://sites.google.com/a/chromium.org/chromedriver/home)
        – Firefox
        – Safari
        – Edge
        – Opera
        
        :param driver: The driver used to navigate through the respective webpage (Moody's/S&P)
        :return: void
    """

    def __init__(self):
        # Nested try-excepts to attempt to use a web browser on the user's local machine
        try:
            try:
                self.driver = webdriver.Chrome('../exec/chromedriver')
            except:
                logger.debug("User does not have Google Chrome")
                try:
                    self.driver = webdriver.Firefox()
                except:
                    logger.debug("User does not have Mozilla Firefox")
                    try:
                        self.driver = webdriver.Safari()
                    except:
                        logger.debug("User does not have Safari")
                        try:
                            self.driver = webdriver.Edge()
                        except:
                            logger.debug("User does not have Microsoft Edge")
                            try:
                                self.driver = webdriver.Opera()
                            except:
                                logger.debug("User does not have Opera")
        except Exception as e:
            logger.error(e)
            return

    """
        Using user's browser as webdriver to get to Moody's Credit Ratings
        :return: The url of the webpage to be scraped as a string, or an error string
    """

    def moodys(self):
        # If any attributes are invalid, the exception should return so that the user can be prompted with a message
        # to request an update/fix to the authors
        try:
            # Go to the website
            driver.get("https://www.moodys.com/")
            # assert "Moody's" in driver.title

            # Find "Ratings News"
            ratingsNews = driver.find_element_by_link_text("Ratings News")
            logger.debug(ratingsNews)
            # Move to Ratings News, hover and click on it, and then click on "Rating Action"
            ratingAction = driver.find_element_by_link_text("Rating Action")
            logger.debug(ratingAction)
            ActionChains(driver).move_to_element(ratingsNews).click().click(ratingAction).perform()

            # After, click on "Corporates"
            corporates = driver.find_element_by_link_text("Corporates")
            logger.debug(corporates)
            corporates.click()

            # Finally, click on "North America" (this program is limited to North American trading/markets)
            country = driver.find_element_by_link_text("North America")
            logger.debug(country)
            country.click()

            # Get the current URL for the spider to crawl
            url = driver.current_url
            logger.debug(url)

            # Close the driver
            driver.close()

            return url
        except Exception as e:
            logger.error(e)
            return e

    """
        Using user's browser as webdriver to get to S&P's Credit Ratings
        :return: The url of the webpage to be scraped as a string, or an error string
    """

    def standardandpoors(self):
        ''' TODO: Implement functionality to enter "Corporates, United States, All (drop downs)
            and "Enter" (link to click)'''
        try:
            # Go to the website
            driver.get("https://www.standardandpoors.com/")

            # First click on "Ratings Actions"
            ratingsActions = driver.find_element_by_name("Ratings Actions")
            ratingsActions.click()

            ratingsActions = driver.find_element_by_name("Ratings Actions")
            ratingsActions.click()

            # Implement functionality to enter "Corporates, United States, All (drop downs)
            # and "Enter" (link to click) below

            ###################################

            # Get the current URL for the spider to crawl
            url = driver.current_url
            logger.info(url)

            # Close the driver
            driver.close()

            return url
        except Exception as e:
            logger.error(e)
            return e