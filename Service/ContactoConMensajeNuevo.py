from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from mongo import guardoContactoMongo

try:
    def esperoClase(wait):
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.RLfQR")))

    def buscoClaseDeMensajesNuevos(driver):
        for person in driver.find_elements_by_class_name('CxUIE'):
            title = person.find_element_by_xpath('div[2]/div[1]/div[1]/span').text
            guardoContactoMongo.guardoContacto(title)


finally:
    pass

