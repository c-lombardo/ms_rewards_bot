# mike_scraper.py
import time
import random
from string import ascii_letters

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

class MikeBot:
    def __init__(self, email, password, driver_path, delay):
        self.email = email
        self.password = password
        #self.driver = webdriver.Chrome(driver_path)
        self.driver = webdriver.Edge(driver_path, capabilities={})
        self.delay = delay

    def login(self):
        self.driver.get("https://rewards.microsoft.com/Signin?idru=%2F")

        # enter email
        username_input_element = WebDriverWait(self.driver, self.delay).until(EC.element_to_be_clickable((By.XPATH, "//*[@type='email']")))
        username_input_element.send_keys(self.email)
        # click next button
        WebDriverWait(self.driver, self.delay).until(EC.element_to_be_clickable((By.XPATH, '//*[@type="submit"]'))).click()

        # enter password
        password_input_element = WebDriverWait(self.driver, self.delay).until(EC.element_to_be_clickable((By.XPATH, "//*[@type='password']")))
        password_input_element.send_keys(self.password)
        # click sign-in button
        WebDriverWait(self.driver, self.delay).until(EC.element_to_be_clickable((By.XPATH, '//*[@type="submit"]'))).click()

        # click "No" for remember me
        WebDriverWait(self.driver, self.delay).until(EC.element_to_be_clickable((By.XPATH, '//*[@value="No"]'))).click()

        time.sleep(5)
    
    def generate_random_president(self):
        with open("./metadata/presidents.txt") as f:
            lines = [line.strip() for line in f.readlines()]
        return random.choice(lines)

    def bing_searches(self, num):
        already_searched = set()
        for i in range(num+1): # first search doesn't get points for some reason
            query = self.generate_random_president()
            while query in already_searched:
                query = self.generate_random_president()
            self.driver.get(f"https://www.bing.com/search?q={query}")
            already_searched.add(query)
            time.sleep(random.randint(10,20))

    def rewards_quizzes(self):
        self.driver.get("https://rewards.microsoft.com/")
        # click 10 points button
        WebDriverWait(self.driver, self.delay).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, '10 points'))).click()

    def quit(self):
    	self.driver.quit()

