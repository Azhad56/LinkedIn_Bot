from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
import os

class LinkedInBot:

    def __init__(self, username, password):
        #For heroku
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--disable-dev-shm-usage")
        # chrome_options.add_argument("--no-sandbox")
        # self.driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        opts = Options()
        opts.set_headless()
        assert opts.headless
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password

    def closeBrowser(self):
        self.driver.close()

    def login(self):
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
        time.sleep(10)
    def connect_people(self):
        driver = self.driver
        count=0
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
                    count += 1
                    print("clicked:",count)
                except Exception:
                    continue
                time.sleep(10)
            time.sleep(5)
