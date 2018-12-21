from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

import sys

# Replace below path with the absolute path
# to chromedriver in your computer
driver = webdriver.Chrome('./chromedriver')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

group_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.RLfQR")))

time.sleep(5)
contactos = list([])

for person in driver.find_elements_by_class_name('CxUIE'):
    title = person.find_element_by_xpath('div[2]/div[1]/div[1]/span').text
    # company = person.find_element_by_xpath('.//div[@class="company"]/a').text
    if title in contactos:
        i = 0
    else:
        contactos.append(title)

for target in contactos:
    target = target
    x_arg = '//span[contains(@title,"' + target + '")]'
    group_title = wait.until(EC.presence_of_element_located((
        By.XPATH, x_arg)))
    group_title.click()


x_arg = '//span[contains(@title,"' + target + '")]'
group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
group_title.click()

for contactos1 in contactos:
    print(contactos1)
