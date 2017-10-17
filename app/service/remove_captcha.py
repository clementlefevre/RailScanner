from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import ipdb
from app.config import URL



CHECKBOX = "recaptcha-checkbox-checkmark"
SEND = "Envoyer"

driver = webdriver.Chrome()
driver.get('https://www.voyages-sncf.com/proposition/rest/')

ipdb.set_trace()
elem = driver.find_element_by_class_name(CHECKBOX)

elem.click()
time.sleep(5)
elem = driver.find_element_by_tag_name(SEND)
elem.send_keys("password")
elem.send_keys(Keys.RETURN)
elem = driver.find_element_by_name(GEHEN)
elem.click()
driver.close()