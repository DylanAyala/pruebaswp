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

print('Contactos')
for contactos1 in contactos:
    print(contactos1)

group_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.vW7d1")))

time.sleep(1)

mensajes = list([])

for person in driver.find_elements_by_class_name('Tkt2p'):
    message = person.find_element_by_xpath('div[1]').text
    mensajes.append(message)

time.sleep(10)

for person in driver.find_elements_by_class_name('Tkt2p'):
    message = person.find_element_by_xpath('div[1]').text
    if title in contactos:
        i = 0
    else:
        contactos.append(title)
print('Mensajes')
for mensajess in mensajes:
    print(mensajess)

message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]

time.sleep(5)
print('Tus mensajes')
string = input("Introducir texto:")

message.send_keys(string)

time.sleep(5)

sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
sendbutton.click()
