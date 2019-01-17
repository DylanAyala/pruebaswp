from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
import insert
import buscoMensaje

target = '+54 9 11 5004-7121'

def localizoContacto(wait):
    x_arg = '//span[contains(@title,"' + target + '")]'
    group_title = wait.until(EC.presence_of_element_located((
        By.XPATH, x_arg)))
    group_title.click()


def localizoMensajes(wait):
    group_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.vW7d1")))


def iteroMensajes(driver):
    for person in driver.find_elements_by_class_name('message-in'):
        message = person.find_element_by_xpath('div/div[1]').text
        hora = person.find_element_by_xpath('div/div[2]/div').text
        resultado = buscoMensaje.realizoQuery(target, message, hora)
        if resultado < 1:
            insert.insert(target, message, hora)
