from pymongo import MongoClient
import json
from datetime import datetime

conection = MongoClient('localhost', 27017)

dataBase = conection['testdb']

collection = dataBase['Contactos']

date = datetime.now()


def buscoElContactoCount(contacto):
    query = json.loads('{"Contacto": "' + contacto + '"}')
    count = collection.count(query)
    return count


def actualizoContacto(contacto):
    query = json.loads('{"Contacto": "' + contacto + '"}')
    querynew = json.loads('{"$set": {"MensajesNuevos": 0}}')
    collection.update_one(query, querynew)


def guardoContacto(contacto):
    query = {"Contacto": contacto, "date": date, "MensajesNuevos": 0}
    collection.insert_one(query)
