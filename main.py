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

    wait.until(EC.visibility_of_element_located((By.ID, "pane-side")))
    try:
        ContactoConMensajeNuevo.esperoClase(wait)
        ContactoConMensajeNuevo.buscoClaseDeMensajesNuevos(driver)
    finally:
        pass

    mensajesNuevos = buscoContactoConMensajesNuevos.buscoContactoConMensajesCount()

    if mensajesNuevos >= 1:
        contacto = buscoContactoConMensajesNuevos.buscoContactoConMensajes()
        for contactos in contacto:
            whatsapp_readmessage2.localizoContacto(wait, contactos["Contacto"])
            whatsapp_readmessage2.localizoMensajes(wait)
            whatsapp_readmessage2.iteroMensajes(driver, contactos["Contacto"])
            buscoContactoConMensajesNuevos.actualizoContacto(contactos["Contacto"])

    count = newMesajeMongo.hayMensajesNuevos()
    if count >= 1:
        for x in newMesajeMongo.buscoMensajesNuevos():
            wait.until(EC.visibility_of_element_located((By.ID, "pane-side")))
            whatsapp_sendmessage.buscoContacto(wait, x["Contacto"])
            whatsapp_sendmessage.escriboYenvio(driver, x["Mensaje"])
            newMesajeMongo.actualizoMensajeEnviado(x["Contacto"], x["Mensaje"])
