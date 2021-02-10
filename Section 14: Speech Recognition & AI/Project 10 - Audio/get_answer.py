import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys, io

class Fetcher:
    def __init__(self, url):
        self.Options = webdriver.ChromeOptions()
        self.Options.set_headless(True)
        self.Options.add_argument("--lang=en-GB")

        self.driver = webdriver.Chrome('C:\Program Files\JetBrains\Pycharm\Section_14\chromedriver.exe', options=self.Options)
        self.driver.wait = WebDriverWait(self.driver, 5)
        self.url = url

    def lookup(self):
        self.driver.get(self.url)
        try:
            ip = self.driver.wait.until(EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "gsfi")
            ))
        except:
            print("Failed to establish connection")

        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        answer = soup.find_all(class_="_sPg")

        if not answer:
            answer = soup.find_all(class_="hgKElc")
        if not answer:
            return "Sorry, I don't know that"
        self.driver.quit()
        return answer[0].get_text()