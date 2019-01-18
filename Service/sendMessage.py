from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def buscoContacto(wait, contacto):
    # Busco contacto e ingreso al chat
    x_arg = '//span[contains(@title,"' + contacto + '")]'
    group_title = wait.until(EC.presence_of_element_located((
        By.XPATH, x_arg)))
    group_title.click()


def escriboYenvio(driver, mensaje):

    # Busco el div que contine el imput para escribir
    message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]

    # Escribo el mensaje
    message.send_keys(mensaje)

    # Envio mensaje
    sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
    sendbutton.click()
