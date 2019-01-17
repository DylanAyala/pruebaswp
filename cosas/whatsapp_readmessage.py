from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

driver = webdriver.Chrome('./chromedriver')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

target = '"+54 9 11 5004-7121"'

time.sleep(5)

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
group_title.click()

time.sleep(5)
group_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.vW7d1")))

time.sleep(1)

mensajes = list([])

for person in driver.find_elements_by_class_name('Tkt2p'):
    message = person.find_element_by_xpath('div[1]').text
    mensajes.append(message)


for mensajess in mensajes:
    print(mensajess)
