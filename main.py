from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Service import whatsapp_readmessage2, whatsapp_sendmessage
from mongo import newMesajeMongo

driver = webdriver.Chrome('./chromedriver')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

while True:

    wait.until(EC.visibility_of_element_located((By.ID, "pane-side")))

    whatsapp_readmessage2.localizoContacto(wait)

    whatsapp_readmessage2.localizoMensajes(wait)

    whatsapp_readmessage2.iteroMensajes(driver)
    count = newMesajeMongo.hayMensajesNuevos()
    if count >= 1:
        for x in newMesajeMongo.buscoMensajesNuevos():
            wait.until(EC.visibility_of_element_located((By.ID, "pane-side")))
            whatsapp_sendmessage.buscoContacto(wait, x["Contacto"])
            whatsapp_sendmessage.escriboYenvio(driver, x["Mensaje"])
            newMesajeMongo.actualizoMensajeEnviado(x["Contacto"], x["Mensaje"])
