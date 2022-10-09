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
import re

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

signIn_button = driver.find_element(By.CSS_SELECTOR, "button[class$='in']")
signIn_button.click()
user = "mytestingaccount@meta.ua"
password = "Bm4BY95U2fI1Kh6"
email = driver.find_element(By.CSS_SELECTOR, "input[name^='e']")
email.send_keys("mytestingaccount@meta.ua")
password = driver.find_element(By.CSS_SELECTOR, "input[name^='p']")
password.send_keys("Bm4BY95U2fI1Kh6")
remember = driver.find_element(By.CSS_SELECTOR, "div[class='form-check']>input[name^='rem']")
remember.click()
loginIn_button = driver.find_element(By.CSS_SELECTOR, "div[class$='content-between']>button[class$='primary']")
loginIn_button.click()

time.sleep(3)
profile_button = driver.find_element(By.CSS_SELECTOR, "a[class*='-profile']")
profile_button.click()
edit_button = driver.find_element(By.CSS_SELECTOR, "div[class$='between']>button[class*='primary']")
edit_button.click()
lastName = driver.find_element(By.CSS_SELECTOR, "input[id*='LastName']")
lastName.click()
lastName.clear()
lastName.send_keys("Popova")
time.sleep(5)
save_button = driver.find_element(By.CSS_SELECTOR, "div[class$='footer']>button[class*='primary']")
save_button.click()

msg = '20.02.1989.'
result = re.match(r'([\d]{2}|[\d]{2}|[\d]{4})', msg)
print(result)
assert result
# assert re.match(r'^Geometry type ".+" is not supported$', msg)

elements = driver.find_elements(By.XPATH, '//input')
print(len(elements))
assert len(elements) > 0

driver.close()