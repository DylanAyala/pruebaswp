from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from mongo import guardoContactoMongo

try:
    def esperoClase(wait):
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div._1rqO1")))


    def buscoClaseDeMensajesNuevos(driver, numero):
        for person in driver.find_elements_by_class_name('CxUIE'):
            title = person.find_element_by_xpath('div[2]/div[1]/div[1]/span').text
            count = guardoContactoMongo.buscoElContactoCount(title, numero)
            if count >= 1:
                guardoContactoMongo.actualizoContacto(title, numero)
            else:
                guardoContactoMongo.guardoContacto(title, numero)

finally:
    pass
