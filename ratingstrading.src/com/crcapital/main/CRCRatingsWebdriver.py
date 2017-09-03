"""
    Property of CR Capital, LLC. All rights reserved.
    Author: Cristian Gonzales
"""

import logging

from selenium import webdriver
from selenium.webdriver.support.ui import Select

"""
    Webdriver used to navigate the respective credit ratings website (Moodys or S&P) and return the url of the
    webpage that needs to be scraped.

    :var myDriver: The global driver to navigate through the respective webpage (Moody's/S&P)
"""

# TODO: Refine S&P webdriver's functionality
class CRCRatingsWebdriver:

    driver = None

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
        # global driver
        global driver
        # Nested try-excepts to attempt to use a web browser on the user's local machine
        try:
            try:
                driver = webdriver.Chrome('../exec/chromedriver')
            except:
                logging.debug("User does not have Google Chrome")
                try:
                    driver = webdriver.Firefox()
                except:
                    logging.debug("User does not have Mozilla Firefox")
                    try:
                        driver = webdriver.Safari()
                    except:
                        logging.debug("User does not have Safari")
                        try:
                            driver = webdriver.Edge()
                        except:
                            logging.debug("User does not have Microsoft Edge")
                            try:
                                driver = webdriver.Opera()
                            except:
                                logging.debug("User does not have Opera")
        except Exception as e:
            logging.error(e)
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

            # Click on "Research and Ratings"
            driver.find_element_by_css_selector("h3").click()
            # Ratings News does not need a WebDriverWait to render since it is on the same page as the CSS selector
            driver.find_element_by_link_text("Ratings News").click()
            # Move to Ratings News, click on it, and then click on "Rating Action"
            driver.find_element_by_xpath(
                "//a[contains(text(),'Rating Action\n')]"
            ).click()
            # After, click on "Corporates"
            driver.find_element_by_css_selector("#mdcOrBrowseBy > ul > li > ul > li > a").click()
            # Finally, click on "North America" (this program is limited to North American trading/markets)
            driver.find_element_by_xpath(
                "//a[contains(text(),'North America\n')]"
            ).click()

            # Get the current URL for the spider to crawl
            url = driver.current_url
            logging.debug(url)

            # Close the driver
            driver.close()
            driver.quit()

            return url

        except Exception as e:
            logging.error(e)
            return e

    """
        Using user's browser as webdriver to get to S&P's Credit Ratings
        :return: The url of the webpage to be scraped as a string, or an error string
    """

    def standardandpoors(self):
        ''' Functionality to enter "Corporates, United States, All (drop downs)
            and "Enter"'''
        try:
            # Go to the S&P US website
            driver.get("https://www.standardandpoors.com/en_US/web/guest/home")

            # First click on "Ratings Actions"
            driver.find_element_by_link_text("Ratings Actions").click()
            # Choose "Corporates" in the drop down box
            Select(driver.find_element_by_id(
                "_rdsmratingsactionportlet_WAR_rdsmratingsactionportlet_ratingssectors")).select_by_visible_text(
                "Corporates")
            # Choose "United States" in the drop down box
            Select(driver.find_element_by_id(
                "_rdsmratingsactionportlet_WAR_rdsmratingsactionportlet_countries_ra")).select_by_visible_text(
                "United States")
            # Click the update button
            driver.find_element_by_id("_rdsmratingsactionportlet_WAR_rdsmratingsactionportlet_Update").click()

            # Get the current URL for the spider to crawl
            url = driver.current_url
            logging.debug("Value of Moody's URL: " + url)

            # Close the driver
            driver.close()
            driver.quit()

            return url

        except Exception as e:
            logging.error(e)
            return e

    """
        This method is used to search the EDGAR SEC webpage and determine if the company is publicly traded
        :param security: The security to be entered into the search bar
        :return: The url of the webpage to be scraped as a string, or an error string
    """
    def edgarSEC(self, security):
        try:
            # Go to the EDGAR SEC website
            driver.get("https://www.sec.gov/edgar/searchedgar/companysearch.html")

            # Go to the search button and enter the appropriate security name into the search box
            driver.find_element_by_id("lesscompany").clear()
            driver.find_element_by_id("lesscompany").send_keys(security)
            driver.find_element_by_id("search_button_1").click()

            # Get the current URL for the spider to crawl
            url = driver.current_url
            logging.debug("Value of current SEC URL: " + url)

            # Close the driver
            driver.close()
            driver.quit()

            return url

        except Exception as e:
            logging.error(e)
            return e