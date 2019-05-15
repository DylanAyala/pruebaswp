from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def buscoContacto(wait, contacto, driver):
    # Busco contacto e ingreso al chat
    # x_arg = '//span[contains(@title,"' + contacto + '")]'
    # group_title = wait.until(EC.presence_of_element_located((
    #   By.XPATH, x_arg)))
    # group_title.click()

    contacto = contacto.replace('+', '')
    contacto = contacto.replace('-', '')
    contacto = contacto.replace(' ', '')
    driver.get("https://api.whatsapp.com/send?phone=" + contacto)
    wait.until(EC.visibility_of_element_located((By.ID, "action-button")))
    test = driver.find_element_by_class_name('button')
    test.click()


def escriboYenvio(driver, mensaje):
    try:
        time.sleep(1)
        # Busco el div que contine el imput para escribir
        message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]

        # Escribo el mensaje
        message.send_keys(mensaje)

        # Envio mensaje
        sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
        sendbutton.click()
    except IndexError:
        print("No se pudo enviar mensaje")
        pass
