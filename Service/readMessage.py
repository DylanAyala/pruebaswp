from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from mongo import buscoMensaje, guardoMensajeMongo


def localizoContacto(wait, contacto):
    # Busca el contacto e ingresa al chat
    x_arg = '//span[contains(@title,"' + contacto + '")]'
    group_title = wait.until(EC.presence_of_element_located((
        By.XPATH, x_arg)))
    group_title.click()


def localizoMensajes(wait):
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.vW7d1")))


def iteroMensajes(driver, contacto):
    # Busca la clase que contiene solo los mensajes entrantes
    for person in driver.find_elements_by_class_name('message-in'):

        # Busca la el div que contiene el texto del mensaje y lo extraigo
        message = person.find_element_by_xpath('div/div[1]').text
        # Busca la el div que contiene la hora del mensaje y lo extraigo
        hora = person.find_element_by_xpath('div/div[2]').text
        # Pregunto si el mensaje ya lo tengo en mi BD
        resultado = buscoMensaje.realizoQuery(contacto, message, hora)
        # Si no tengo el mensaje en BD lo inserto
        if resultado < 1:
            guardoMensajeMongo.insert(contacto, message, hora)


def respuestasMensajes(driver):
    for respuesta in driver.find_elements_by_class_name('_3CVlE'):
        mensajeDeRespuesta = respuesta.find_element_by_xpath('div/div/div/div/div[2]/span').text
        return mensajeDeRespuesta
