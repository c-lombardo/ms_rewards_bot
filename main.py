# main.py
import mike_scraper
import mobile_mike_scraper
import time
import random

MSEDGE_DRIVER_PATH = "./msedgedriver"
CHROME_DRIVER_PATH = "./chromedriver"
DELAY = 15

# pull metadata
with open("./metadata/email.txt") as f:
	lines = [line.strip() for line in f.readlines()]
EMAIL = lines[0]
with open("./metadata/password.txt") as f:
	lines = [line.strip() for line in f.readlines()]
PASS = lines[0]

# complete mobile searches
mobile_mike = mobile_mike_scraper.MobileMikeBot(EMAIL, PASS, CHROME_DRIVER_PATH, DELAY)
mobile_mike.login()
mobile_mike.bing_searches(random.randint(25,35))
mobile_mike.quit()

# complete desktop searchs
mike = mike_scraper.MikeBot(EMAIL, PASS, MSEDGE_DRIVER_PATH, DELAY)
mike.login()
mike.bing_searches(random.randint(35,45))

# complete rewards quizzes
mike.rewards_quizzes()
mike.quit()