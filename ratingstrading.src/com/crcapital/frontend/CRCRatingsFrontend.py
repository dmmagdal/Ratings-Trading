"""
    Property of CR Capital, LLC. All rights reserved.
    Author: Bill Patterson
"""
import logging

from PIL import ImageTk, Image

import sys

import tkinter
from tkinter import messagebox
from tkinter import Label
from tkinter import Frame
from tkinter import IntVar
from tkinter import Radiobutton
from tkinter import Button
from tkinter import Tk

from com.crcapital.ratingscrawler.ratingscrawler.CRCRatingsPair import CRCRatingsPair

"""
    Front end constructor that is passed the array of CRCRatingsPairs (ADT to abstract the tickers and statuses).
    Here, it is initialized such that each frame is a module.
"""
class CRCRatingsFrontend(tkinter.Frame):

    """
        Aformentioned constructor mentioned in last comment. Seperate thread initialized in CRCRatingsMoodys.
        :param arrayOfPairs: This is the array of CRCRatingPairs, as passed by the thread declaration in
        CRCRatingsMoodys
    """
    def __init__(self, arrayOfPairs):

        # Array of CRCRatingsPair objects
        self.arrayOfPairs = arrayOfPairs

        # Hardcoded width and height (for now)...
        self.width = "375"
        self.height = "500"

        # Root initialization
        self.root = Tk()
        self.root.title("Ratings-Trading")
        self.root.geometry(self.width + "x" + self.height)
        self.mainFrame(self.root)

        # While true, keep the application visible. Protocal calling on_closing to properly close the window
        # and terminate the thread
        # TODO: Fix this (properly closing the thread)!
        # self.root.protocol("WM_DELETE_WINDOW", self.on_closing())
        self.root.mainloop()

    """
        This is the main frame, and hence the first window that pops up once the prior threads are terminated.
        This is the last thread in the sequence of threads in CRCRatingsMoodys.
        :param master: Tk() variable
    """
    def mainFrame(self, master):

        # Main frame
        frame = Frame(master)
        frame.pack()

        # CRC logo
        sys.path.append('../../../../CRC_Logo.png')
        img = ImageTk.PhotoImage(Image.open("../../../../CRC_Logo.png"))
        # TODO: Fix icon
        # master.iconbitmap("../../../../CRC_Logo.ico")
        img_panel = Label(master, image=img)
        img_panel.image = img
        img_panel.pack()

        banner = Label(master, text='Welcome to the Ratings Trader', font=('Helvetica', 24))
        banner.pack(side="bottom", fill="both", expand="yes")

        choose_brokerage_label = Label(master,text='Choose your brokerage:')
        choose_brokerage_label.pack()

        # Engineered in such a way that one can add more brokerages (in the form of radio buttons) if
        # further functionality is sought. For now, this is more of a proof of concept than a product,
        # so for those reasons, interfacing with other brokerage APIs is not a priority.

        # Tkinter variable to determine callback values
        self.selection = IntVar()

        no_selection = Radiobutton(master, text='[None]', variable=self.selection, value = 0,
                                   command=self.selection_callback)
        no_selection.pack()
        IB_selection = Radiobutton(master, text='Interactive Brokers', variable=self.selection,
                                   value=1, command=self.selection_callback)
        IB_selection.pack()

        more = Label(master, text='More brokerages to come...')
        more.pack()

        next = Button(master, text='Next')
        next.pack()

    """
        This is the callback initiated when a RadioButton is selected
        0 - [None]
        1 - [Interactive Brokers]
        ...
        (More brokerages may be added in the future)
    """
    def selection_callback(self):
        logging.debug(str(self.selection.get()))

    """
        This is the on_closing protocol that will properly destroy the application, such that the main thread in
        the spider can resume.
    """
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            self.root.destroy()