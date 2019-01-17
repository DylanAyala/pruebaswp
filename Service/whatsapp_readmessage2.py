from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from mongo import buscoMensaje, insert


def localizoContacto(wait, contacto):
    x_arg = '//span[contains(@title,"' + contacto + '")]'
    group_title = wait.until(EC.presence_of_element_located((
        By.XPATH, x_arg)))
    group_title.click()


def localizoMensajes(wait):
    group_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.vW7d1")))


def iteroMensajes(driver, contacto):
    for person in driver.find_elements_by_class_name('message-in'):
        message = person.find_element_by_xpath('div/div[1]').text
        hora = person.find_element_by_xpath('div/div[2]/div').text
        resultado = buscoMensaje.realizoQuery(contacto, message, hora)
        if resultado < 1:
            insert.insert(contacto, message, hora)
