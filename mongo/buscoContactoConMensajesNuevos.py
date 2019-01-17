from pymongo import MongoClient
import json
from datetime import datetime

conection = MongoClient('localhost', 27017)

dataBase = conection['testdb']

collection = dataBase['Contactos']


def buscoContactoConMensajesCount():
    query = json.loads('{"MensajesNuevos": 0}')
    count = collection.count(query)
    return count


def buscoContactoConMensajes():
    query = json.loads('{"MensajesNuevos": 0}')
    resultado = collection.find(query)
    return resultado


def actualizoContacto(contacto):
    query = json.loads('{"Contacto": "' + contacto + '"}')
    querynew = json.loads('{"$set": {"Contacto": "' + contacto + '","MensajesNuevos": 1}}')
    collection.update_one(query, querynew)
