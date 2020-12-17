from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as E
from env import  sensitiveData

loginid = sensitiveData.login
password = sensitiveData.password

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
actions = ActionChains(driver)

driver.get("https://student.amizone.net")
print(driver.title)

search = driver.find_element_by_name('_UserName')
search1 = driver.find_element_by_name('_Password')
search.send_keys(loginid)
search1.send_keys(password)

search.send_keys(Keys.RETURN)

time.sleep(10)
driver.quit()