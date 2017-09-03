"""
    Property of CR Capital, LLC. All rights reserved.
    Author: Bill Patterson
"""
import tkinter
from tkinter import Label
from tkinter import Frame
from tkinter import StringVar
from tkinter import Radiobutton
from tkinter import Button
from tkinter import Tk

class CRCRatingsFrontend(tkinter.Frame):

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        banner = Label(master, text='Welcome to the Ratings Trader!', font=('Helvetica', 24))
        banner.pack()

        choose_brokerage = Label(master,text='Choose your brokerage:')
        choose_brokerage.pack()

        brokerage = StringVar()
        brokerage_selection = Radiobutton(master, text='Interactive Brokers', variable=brokerage, value='Interactive Brokers')
        brokerage_selection.pack()

        more = Label(master, text='More brokerages to come...')
        more.pack()

        next = Button(master, text='Next')
        next.pack()

root = Tk()

app = CRCRatingsFrontend(root)

root.mainloop()