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


def leer():
    for person in driver.find_elements_by_class_name('_2wP_Y'):
        title = person.find_element_by_xpath('div/div/div[2]/div[1]/div[1]/span').text
        # company = person.find_element_by_xpath('.//div[@class="company"]/a').text
        if title in contactos:
            i = 0
        else:
            contactos.append(title)


def leerLoop():
    group_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div._2wP_Y")))
    for person1 in driver.find_elements_by_class_name('_2wP_Y'):
        person1.click()
        i = 0
        i += 1
        if i == 2:
            group_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div._2wP_Y")))
            for person in driver.find_elements_by_class_name('_2wP_Y'):
                title = person.find_element_by_xpath('div/div/div[2]/div[1]/div[1]/span').text
                # company = person.find_element_by_xpath('.//div[@class="company"]/a').text
                if title in contactos:
                    i = 0
                else:
                    contactos.append(title)
    return


def ultimo(target):
    x_arg = '//span[contains(@title,"' + target + '")]'
    group_title = wait.until(EC.presence_of_element_located((
        By.XPATH, x_arg)))
    group_title.click()


def leeer():
    target = contactos[-1]
    ultimo(target)
    leer()


leer()

target = contactos[2]

contactoU = contactos[-1]

ultimo(target)

leer()

contactoU2 = contactos[-1]

while contactoU != contactoU2:
    leeer()
    contactoU = contactos[-1]
    leeer()
    contactoU2 = contactos[-1]


for contactos1 in contactos:
    print(contactos1)
