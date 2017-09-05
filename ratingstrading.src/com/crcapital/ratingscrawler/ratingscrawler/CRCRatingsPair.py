"""
    Property of CR Capital, LLC. All rights reserved.
    Author: Cristian Gonzales
"""

import logging
import requests
import re

"""
    This is the ADT that will store the acting key-value pair for the status of the company (upgrade or
    downgrade), the name of the company, and the ticker of the company (for the purposes of querying for
    orders using the IB API). This object will act as one key-value pair, and is intended to be stored
    in an array of CRCRatingPairs.
"""
class CRCRatingsPair:

    def __init__(self):
        return

    """
        :param name: The name of the security
        :return void
    """
    def set_name(self, name):
        self.name = name

    """
        :return name: the name of the security
    """
    def get_name(self):
        try:
            return self.name
        except Exception as e:
            logging.error(e)
            return

    """
    :param status: The status of the security (upgrade/downgrade)
    :return void
    """
    def set_status(self, status):
        self.status = status

    """
        :return status: the status of the security
    """
    def get_status(self):
        try:
            return self.status
        except Exception as e:
            logging.error(e)
            return

    """
        Conversion from name to ticker using JSON. Precondition: name should already be initialized.
        Credit:
        https://stackoverflow.com/questions/38967533/retrieve-company-name-with-ticker-symbol-input-yahoo-or-google-api
        (@masnun)
        :return void
    """
    def set_ticker(self):

        # Initial value of ticker class variable to be "N/A"
        self.ticker = "None"

        try:
            # Quick hard-coded hack, betting on the corporation name being more than two words long. With this,
            # querying the Yahoo Finance DB for the ticker name will be much easier. More robust functionality with
            # this is a minute but important feature that may be explored in the future.
            name = re.split(' |, ', self.name)
            logging.debug("name[0]: " + name[0])
            logging.debug("name[1]: " + name[1])
            corp_name = name[0] + " " + name[1]
            # url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(self.name)
            url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(corp_name)
            logging.debug("URL: " + url)
            result = requests.get(url).json()
            logging.debug("JSON: " + str(result))

            # For the resulting JSON, if the company is publicly traded and the parsed down company name is in
            # the JSON attribute "name", then make the ticker class variable equal to the value for the
            # JSON attribute "symbol"
            # The ticker will be initialized to "N/A" if no matches are ever found
            for x in result['ResultSet']['Result']:
                if corp_name in x['name'] and (x['exchDisp'] == 'NYSE' or x['exchDisp'] == 'NASDAQ'):
                    self.ticker = x['symbol']

            logging.debug("Ticker: " + self.ticker)

        except Exception as e:
            logging.error(e)

    """
        :return ticker: the ticker of the security
    """
    def get_ticker(self):
        try:
            return self.ticker
        except Exception as e:
            logging.error(e)