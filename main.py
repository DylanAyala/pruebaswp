from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Service import readMessage, sendMessage, ContactoConMensajeNuevo, guardoNumero
from mongo import newMesajeMongo, buscoContactoConMensajesNuevos
import time

driver = webdriver.Chrome('./Driver/chromedriver')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
# Espero a que cargue el panel
wait.until(EC.visibility_of_element_located((By.ID, "pane-side")))
# Extraigo la imagen de perfil para saber el numero
numero = guardoNumero.extraigoNumero(driver)

while True:
    time.sleep(2)
    # Busco el Panel del los Contactos para setear el inicio de las busquedas
    wait.until(EC.visibility_of_element_located((By.ID, "pane-side")))
    try:

        # Espera la clase que contiene cada contacto
        ContactoConMensajeNuevo.esperoClase(wait)

        # Busca si hay contactos que contengan la clase de mensajes nuevos
        ContactoConMensajeNuevo.buscoClaseDeMensajesNuevos(driver, numero)
    finally:
        pass

    try:

        # Busca si hay un contacto en Mongo sin Leer los mensajes Nuevos
        mensajesNuevos = buscoContactoConMensajesNuevos.buscoContactoConMensajesCount(numero)

        if mensajesNuevos >= 1:

            # Trea todos los contactos con mensajes Nuevos
            contacto = buscoContactoConMensajesNuevos.buscoContactoConMensajes(numero)
            for contactos in contacto:
                # Leo los Mensajes y los Guardo en Mongo
                readMessage.localizoContacto(wait, contactos["contacto"])
                readMessage.localizoMensajes(wait)
                readMessage.iteroMensajes(driver, contactos["contacto"], numero)
                buscoContactoConMensajesNuevos.actualizoContacto(contactos["contacto"], numero)

        # Busca en Mongo si hay mensajes para enviar
        count = newMesajeMongo.hayMensajesNuevos(numero)
        if count >= 1:

            # traigo los mensajes pendientes para enviar
            for x in newMesajeMongo.buscoMensajesNuevos(numero):
                sendMessage.buscoContacto(wait, x["contacto"], driver)
                # Busco contacto para enviar y envio mensaje
                wait.until(EC.visibility_of_element_located((By.ID, "pane-side")))
                sendMessage.escriboYenvio(driver, x["mensaje"])
                newMesajeMongo.actualizoMensajeEnviado(x["contacto"], x["mensaje"], numero)
    finally:
        pass
