from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument("--no-sandbox")
# options.add_argument("headless")

# START DRIVER
# driver = webdriver.Chrome('/Users/kristina/Downloads/chromedriver', options=options)
# driver = webdriver.Chrome(service=Service('/Users/kristina/Downloads/chromedriver'), options=options)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://qauto2.forstudy.space/")

user = "guest"
password = "welcome2qauto"
driver.get("https://"+user+":"+password+"@"+"qauto2.forstudy.space/")

# SignIn
signIn_button = driver.find_element(By.XPATH, "//button[@class='btn btn-outline-white header_signin']")
signIn_button.click()
user = "mytestingaccount@meta.ua"
password = "Bm4BY95U2fI1Kh6"
email = driver.find_element(By.XPATH, "//input[@id='signinEmail']")
email.send_keys("mytestingaccount@meta.ua")
password = driver.find_element(By.XPATH, "//input[@id='signinPassword']")
password.send_keys("Bm4BY95U2fI1Kh6")
remember = driver.find_element(By.XPATH, "//input[@id='remember']")
remember.click()
loginIn_button = driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
loginIn_button.click()

time.sleep(2)  # sleep for 2 sec
assert "My profile" in driver.page_source

driver.close()