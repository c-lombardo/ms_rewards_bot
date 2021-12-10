# mobile_mike_scraper.py
import mike_scraper

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class MobileMikeBot(mike_scraper.MikeBot):
    def __init__(self, email, password, driver_path, delay):
        self.email = email
        self.password = password
        chrome_options = Options()
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
        self.driver = webdriver.Chrome(driver_path, options=chrome_options)
        self.delay = delay
