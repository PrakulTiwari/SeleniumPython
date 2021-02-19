from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as E
from env import sensitiveData
from selenium.webdriver.support.select import Select
import random
loginid = sensitiveData.loginid
loginpassword = sensitiveData.loginpassword
email_list = ['@outlook.com', '@yahoo.in', '@yahoo.com',
              '@gmail.com', '@amity.edu', '@hotmail.com']

PATH = sensitiveData.driverpath

f = open("name.txt", "r")
for x in f:
    driver = webdriver.Chrome(PATH)
    actions = ActionChains(driver)
    random_email = random.choice(email_list)
    rn_email_no = random.randrange(2, 296)
    driver.get("https://www.cleannoida.org/zerowaste/")
    time.sleep(2)
    search = driver.find_element_by_id('take-pledge')
    search.click()
    name = driver.find_element_by_id('nc_fullname')
    gender = driver.find_element_by_id('female')
    email = driver.find_element_by_id('nc_email')
    state = driver.find_element_by_id('nc_state')
    select_object1 = Select(state)
    # haryana = driver.find_element_by_value('haryana')
    city = driver.find_element_by_id('nc_city')
    select_object2 = Select(city)

    # faridabad = driver.find_element_by_value('faridabad')
    tick1 = driver.find_element_by_id('nc_receiveupdates')
    tick2 = driver.find_element_by_id('nc_volunteeraccount')
    proceed = driver.find_element_by_id('proceed-read')
    proceed2 = driver.find_element_by_id('proceed-cirti')
    download = driver.find_element_by_id('pdfpath')
    final_email = x.lower()+str(rn_email_no) + str(random_email)
    e = open('email.txt', 'a+')
    e.writelines(final_email+'\n')
    print(final_email)
    name.send_keys(x)
    email.send_keys(final_email)
    gender.click()
    select_object1.select_by_visible_text('Uttar Pradesh')
    time.sleep(1)
    select_object2.select_by_visible_text('Noida')
    tick1.click()
    tick2.click()
    proceed.click()
    time.sleep(1)
    proceed2.click()
    time.sleep(4)
    download.click()
    time.sleep(3)
    driver.quit()
    time.sleep(2)
# haryana.click()
# city.click()
# faridabad.click()
# search = driver.find_element_by_name('_UserName')
# search1 = driver.find_element_by_name('_Password')
# search.send_keys(loginid)
# search1.send_keys(loginpassword)

# search.send_keys(Keys.RETURN)

# time.sleep(5)

# try:
#     close = driver.find_element_by_css_selector('button.close')
#     close.Click()
# except:
#     try:
#         close = driver.find_element_by_css_selector('button.close')
#         actions.MoveToElement(close)
#         actions.Click(close)
#         actions.perform()
#     except:
#         print('Could not close popup😢')

# time.sleep(10)
# driver.quit()
