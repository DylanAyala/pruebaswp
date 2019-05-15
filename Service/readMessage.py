from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from mongo import buscoMensaje, guardoMensajeMongo
from urllib.request import urlretrieve
import urllib3
import time


def localizoContacto(wait, contacto):
    # Busca el contacto e ingresa al chat
    x_arg = '//span[contains(@title,"' + contacto + '")]'
    group_title = wait.until(EC.presence_of_element_located((
        By.XPATH, x_arg)))
    group_title.click()


def localizoMensajes(wait):
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.vW7d1")))


def iteroMensajes(driver, contacto, numero):
    # Busca la clase que contiene solo los mensajes entrantes
    for person in driver.find_elements_by_class_name('message-in'):
        # Busca la el div que contiene el texto del mensaje y lo extraigo
        message = person.find_element_by_xpath('div/div[1]').text
        # Busca la el div que contiene la hora del mensaje y lo extraigo
        hora = person.find_element_by_xpath('div/div[2]').text
        #if message == '':
         #   message = leerEmoji(driver, contacto, hora)
        # Pregunto si el mensaje ya lo tengo en mi BD
        resultado = buscoMensaje.realizoQuery(contacto, message.replace('\n', '-> ').replace('\r', ''), hora, numero)
        # Si no tengo el mensaje en BD lo inserto
        if resultado < 1:
            guardoMensajeMongo.insert(contacto, message, hora, numero)


def leerEmoji(driver, contacto, hora):
    # busca la clase que contiene las imagenes
    images = driver.find_elements_by_class_name('_2DV1k')
    for image in images:
        # # Extra el SRCde la imagen
        # src = image.get_attribute('src')
        # timeNow = time.strftime("%d-%m-%Y")
        # path = "./public/emojis/"
        # png = "emoji.png"
        # # Guardo la imagen
        # urlretrieve(src, path + contacto + hora.replace(':', '-') + timeNow + src[29:200])
        # return path + contacto + hora.replace(':', '-') + timeNow + src[29:200]
        image.click()
        dowloads = driver.find_elements_by_class_name('_3TbsN')
        dowloads.click()
        return "hola"


def leerEmoji2(person, contacto, hora):
    # busca la clase que contiene las imagenes
    images = person.find_elements_by_xpath('div/div[1]/div/div/span/img')

    image = images.urllib.request.urlopen(images.get_attribute('src'))
    date = image.read()

    timeNow = time.strftime("%d-%m-%Y")
    path = "./public/emojis/"
    png = "emoji.png"
    with open(path + contacto + hora.replace(':', '-') + timeNow + png, 'wb') as f:
        f.write(date)

    return path + contacto + hora.replace(':', '-') + timeNow + png
