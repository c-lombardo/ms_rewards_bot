# main.py
import mike_scraper
import mobile_mike_scraper
import time
import random

MSEDGE_DRIVER_PATH = "./msedgedriver"
CHROME_DRIVER_PATH = "./chromedriver"
DELAY = 60

# pull metadata
logins = {}
with open("./metadata/login_info.txt") as f:
	lines = [line.strip() for line in f.readlines()]
for line in lines:
	spl = line.split()
	logins[spl[0]] = spl[1]

for email in logins:
	# complete mobile searches
	print("Searching on mobile from " + email)
	mobile_mike = mobile_mike_scraper.MobileMikeBot(email, logins[email], CHROME_DRIVER_PATH, DELAY)
	mobile_mike.login()
	mobile_mike.bing_searches(random.randint(25,35))
	mobile_mike.quit()

	# complete desktop searches and rewards quizzes
	print("Searching on desktop and doing rewards quizzes from " + email)
	mike = mike_scraper.MikeBot(email, logins[email], MSEDGE_DRIVER_PATH, DELAY)
	mike.login()
	mike.bing_searches(random.randint(35,45))
	mike.rewards_quizzes()
	mike.quit()

	print()