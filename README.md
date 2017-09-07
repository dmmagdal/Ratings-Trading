# Ratings-Trading

## Authors: Cristian Gonzales (@cristiangonzales) <xcristian.gonzales@gmail.com>, Bill Patterson (@bpatterson500) <clarinet500@gmail.com>

> Property of CR Capital, LLC. All rights reserved.
> Unauthorized copying of these files, via any medium is strictly prohibited.
> Proprietary and confidential.
> Written by Cristian Gonzales <xcristian.gonzales@gmail.com>, September 2017

![](CRC_Logo.png)

# Summary
Trading credit ratings when companies get upgraded/downgraded on Moody's and S&P. Interfaces with Interactive Brokers API, and Scrapy, Selenium, and Tkinter frameworks. Also employs Matplotlib library to visualize trading performance on the frontend.

# Usage
* To use, download the Interactive Brokers Trader Workstation (IB TWS) for your desktop and open an Interactive Brokers account. Upon doing so, open the desktop app and navigate through the application.
* It is **mandatory** that the application is open before market hours (9:30 AM to 4:00 PM EST)
* The desktop application will prompt for you to select which credit agency you would like to employ for credit upgrades/downgrades for the day (Moody's or S&P)
* Upon selecting the credit agency, the respective publicly traded companies and their share price will be listed. With this, you will be able to enter the amount of shares you would like to trade for each company.
* With this, all you need to do is keep the desktop app on idle or run in the background, and it will dump all the bought shares (or cover the short) and terminate by 4:00 PM EST. There will also be an option to track performance using real-time data.
* The application is to be used on a day-to-day basis. 
* If there are any issues, please submit a fix request.
* **As it stands, this is a work in-progress and a fully functional UI has not yet been develop. As we are in the early stages in development, you may currently run CRCRatingsMain in the "main" subdirectory to track the application's current progress.**

# Misc. Notes
* As of now, the only tested functionality is with the Google Chrome web browser.
* As mentioned, there is potential to feature other brokerages that offer open source APIs.
* There is work to be done on the frontend as well.

# Known bugs
* Thread that initiates the frontend causes the spider to have an error.

# Todos
* Fix the desktop/application icon

# Functionality to be explored in the future
* Because this is a proof of concept, other functionality with other brokerage will not be implemented at this time, but perhaps at another time.
* Functionality with iOS and Android is something that can be explored in the future for this application. Though, to explore functionality with other trading workstations from different sources, we are currently focused on building around Desktop applications.
* Full automation so that the application is open in the background while the machine is on, such that it will "auto-trade," so to speak, on a day-to-day basis (this is an option we are exploring in the near future). Tensorflow is an option in exploring the applications of ML to automating the process for traders and financial analyst, as ML/Data Analytics persists in the industry.
