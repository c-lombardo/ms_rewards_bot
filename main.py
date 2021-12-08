# main.py
import mike_scraper
import time

DRIVER_PATH = "./msedgedriver"
DELAY = 15

# pull metadata
with open("./metadata/email.txt") as f:
	lines = [line.strip() for line in f.readlines()]
EMAIL = lines[0]
with open("./metadata/password.txt") as f:
	lines = [line.strip() for line in f.readlines()]
PASS = lines[0]


mike = mike_scraper.MikeBot(EMAIL, PASS, DRIVER_PATH, DELAY)
mike.login()
#mike.bing_searches(15)
mike.rewards_quizzes()
#mike.quit()