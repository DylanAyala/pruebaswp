from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Service import whatsapp_readmessage2, whatsapp_sendmessage
from mongo import newMesajeMongo
from Service import ContactoConMensajeNuevo
from mongo import buscoContactoConMensajesNuevos

driver = webdriver.Chrome('./chromedriver')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

while True:

    # Busco el Panel del los Contactos para setear el inicio de las busquedas
    wait.until(EC.visibility_of_element_located((By.ID, "pane-side")))
    try:

        # Espera la clase que contiene cada contacto
        ContactoConMensajeNuevo.esperoClase(wait)

        # Busca si hay contactos que contengan la clase de mensajes nuevos
        ContactoConMensajeNuevo.buscoClaseDeMensajesNuevos(driver)
    finally:
        pass

    try:

        # Busca si hay un contacto en Mongo sin Leer los mensajes Nuevos
        mensajesNuevos = buscoContactoConMensajesNuevos.buscoContactoConMensajesCount()

        if mensajesNuevos >= 1:

            # Trea todos los contactos con mensajes Nuevos
            contacto = buscoContactoConMensajesNuevos.buscoContactoConMensajes()
            for contactos in contacto:
                # Leo los Mensajes y los Guardo en Mongo
                whatsapp_readmessage2.localizoContacto(wait, contactos["Contacto"])
                whatsapp_readmessage2.localizoMensajes(wait)
                whatsapp_readmessage2.iteroMensajes(driver, contactos["Contacto"])
                buscoContactoConMensajesNuevos.actualizoContacto(contactos["Contacto"])

        # Busca en Mongo si hay mensajes para enviar
        count = newMesajeMongo.hayMensajesNuevos()
        if count >= 1:

            # traigo los mensajes pendientes para enviar
            for x in newMesajeMongo.buscoMensajesNuevos():
                # Busco contacto para enviar y envio mensaje
                wait.until(EC.visibility_of_element_located((By.ID, "pane-side")))
                whatsapp_sendmessage.buscoContacto(wait, x["Contacto"])
                whatsapp_sendmessage.escriboYenvio(driver, x["Mensaje"])
                newMesajeMongo.actualizoMensajeEnviado(x["Contacto"], x["Mensaje"])
    finally:
        pass
