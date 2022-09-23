# sandbox.py
import mike_scraper
import mobile_mike_scraper
import time
import random

MSEDGE_DRIVER_PATH = "./msedgedriver"
CHROME_DRIVER_PATH = "./chromedriver"
DELAY = 15

email = "christopheranlombardo@gmail.com"
pw = "Rocknblues0"

'''
mobile_mike = mobile_mike_scraper.MobileMikeBot(email, pw, CHROME_DRIVER_PATH, DELAY)
mobile_mike.login()
mobile_mike.bing_searches(2)
'''

mike = mike_scraper.MikeBot(email, pw, MSEDGE_DRIVER_PATH, DELAY)
mike.login()
mike.bing_searches(2)