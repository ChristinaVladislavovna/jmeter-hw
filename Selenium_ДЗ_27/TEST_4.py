from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--no-sandbox")
# options.add_argument("headless")

# START DRIVER
# driver = webdriver.Chrome('/Users/kristina/Downloads/chromedriver', options=options)
# driver = webdriver.Chrome(service=Service('/Users/kristina/Downloads/chromedriver'), options=options)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://qauto2.forstudy.space")

user = "guest"
password = "welcome2qauto"
driver.get("https://"+user+":"+password+"@"+"qauto2.forstudy.space/")

def is_element_present(self, how, what):  #функція
    try:
        self.driver.find_element(by=how, volue=what)
    except NoSuchElementException as e:
        return False
    return True

element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn header-link']"))).click()

assert "Log fuel expenses" in driver.page_source
print("Assert - Correct")
driver.close()