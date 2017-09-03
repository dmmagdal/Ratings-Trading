"""
    Property of CR Capital, LLC. All rights reserved.
    Author: Cristian Gonzales
"""

import logging

import requests

"""
    This is the ADT that will store the acting key-value pair for the status of the company (upgrade or
    downgrade), the name of the company, and the ticker of the company (for the purposes of querying for
    orders using the IB API). This object will act as one key-value pair, and is intended to be stored
    in an array of CRCRatingPairs.
"""
class CRCRatingsPair:
    global status, name, ticker

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
            return name
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
            return status
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
        try:
            url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(name)

            result = requests.get(url).json

            for x in result['ResultSet']['Result']:
                if x['name'] == name:
                    self.ticker = x['symbol']

        except Exception as e:
            logging.error(e)
            return

    """
        :return ticker: the ticker of the security
    """
    def get_ticker(self):
        try:
            return ticker
        except Exception as e:
            logging.error(e)
            return