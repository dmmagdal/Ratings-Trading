"""
Property of CRCapital, all rights reserved.
Author: Bill Patterson

This is a script to interface with the interactive brokers API for buying and selling securities
using the Trader's Workstation

"""

import ib

import ib.ext.Contract
import ib.ext.Order


# Function to gather information about the security, which creates a "Contract"

def make_contract(symbol, sec_type, exch, prim_exch, curr):
    ib.ext.Contract.Contract.m_symbol = symbol
    ib.ext.Contract.Contract.m_secType = sec_type
    ib.ext.Contract.Contract.m_exchange = exch
    ib.ext.Contract.Contract.m_primaryExch = prim_exch
    ib.ext.Contract.Contract.m_currency = curr
    return ib.ext.Contract.Contract


# Function to gather information about the action to be performed on the security, called an "Order"

def make_order(action, quantity, price=None):
    if price is not None:
        order = Order()
        order.m_orderType = 'LMT'
        order.m_totalQuantity = quantity
        order.m_lmtPrice = price

    else:
        order = Order()
        order.m_orderType = 'MKT'
        order.m_totalQuantity = quantity

    return order


cid = 303

# Gathers arguments for make_contract() and make_order() functions
ticker = input("Please input the ticker symbol of the security you would like to trade: ")
ticker = ticker.upper()
order_action = input("Would you like to buy or sell? (B/S) ")
if (order_action == 'B'):
    order_action = 'BUY'
elif (order_action == 'S'):
    order_action = 'SELL'
number_positions = input("How many positions would you like to trade? ")
number_positions = int(number_positions)

type_order = input("Would you like to make a limit order or market order? (LMT/MKT) ")

if (type_order == 'LMT'):
    price_per_position = input("What is the price per position you would like to trade at?")
    price_per_position = int(price_per_position)

elif (type_order == 'MKT'):
    price_per_position = None

else:
    print("Please enter either 'LMT' or 'MKT'")


# Connects to IB API to place buy/sell order

# TODO: Fix issue with not being able to import Connection module


while __name__ == "__main__":
    conn = Connection.create(port=7496, clientID=83625)
    conn.connect()
    oid = cid
    cont = make_contract(ticker, 'STK', 'SMART', 'SMART', 'USD')
    order = make_order(order_action, number_positions, price_per_position)
    conn.placeOrder(oid, cont, order)
    conn.disconnect()
    x = input('enter to resend')
    cid += 1
