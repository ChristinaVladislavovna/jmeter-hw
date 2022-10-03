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

element = driver.find_element(By.XPATH, "//a[@class='btn header-link -active']") #this element is visible
if element.is_displayed():
    print("Element found")
    not_found = True
else:
    print("Element not found")
    not_found = False

assert "hillel" in driver.page_source
if element.is_displayed():
    print("logo present")
driver.close()