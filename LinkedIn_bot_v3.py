from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
import random
import sys

class LinkedInBot:

    def __init__(self, username, password):
        opts = Options()
        opts.set_headless()
        assert opts.headless
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(options=opts)

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        print("Hey")
        driver = self.driver
        driver.get("https://www.linkedin.com/")
        time.sleep(4)
        driver.maximize_window()
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//*[@id='session_key']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        time.sleep(2)
        passworword_elem = driver.find_element_by_xpath("//*[@id='session_password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        time.sleep(2)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(15)
    def connect_people(self):
        driver = self.driver
        while True:
            driver.get("https://www.linkedin.com/mynetwork/")
            time.sleep(4)
            driver.find_element_by_xpath("//*[@id='msg-overlay']/div[1]/header/section[1]").click()
            time.sleep(4)
            for i in range(2):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
            time.sleep(5)
            all = driver.find_elements_by_xpath("//button[@data-test-person-connect='true']/span")
            time.sleep(5)
            for people in all:
                try:
                    people.click()
                    print("clicked")
                except Exception:
                    continue
                time.sleep(30)
            time.sleep(60)
