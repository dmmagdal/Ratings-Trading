# Property of CR Capital, LLC. All rights reserved.
# Author: Bill Patterson

# Prints ticker symbols for Google, Apple, and Amazon
print(
    '\n GOOG'
    '\n AAPL'
    '\n AMZN'
)

# Creating a trade class

class Trade():
    """A class designed to gather information about the trade a user would like to place"""

    def __init__(self, security, price_per_position, number_positions):
        """Initialize security, price_per_position, and number_positions attributes"""
        self.security = security
        self.price_per_position = price_per_position
        self.number_positions = number_positions

    def place_trade(self):
        """Gather information about the trade"""
        print("You are trading " + self.number_positions + " shares of " + self.security.capitalize() + " at " + self.price_per_position + " dollars per share.")

user_security = input("Which security would you like to trade?")
user_price_per_position = input("What is the price per position?")
user_number_positions = input("How many positions would you like to buy?")

Trade(user_security,user_price_per_position,user_number_positions).place_trade()