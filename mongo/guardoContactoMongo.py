from pymongo import MongoClient
import json
from datetime import datetime

conection = MongoClient('localhost', 27017)

dataBase = conection['testdb']

collection = dataBase['Contactos']

date = datetime.now()


def buscoElContactoCount(contacto, numero):
    query = json.loads('{"contacto": "' + contacto + '", "origen": ' + numero + '}')
    count = collection.count(query)
    return count


def actualizoContacto(contacto, numero):
    query = json.loads('{"contacto": "' + contacto + '", "origen": ' + numero + '}')
    querynew = json.loads('{"$set": {"mensajesNuevos": 0}}')
    collection.update_one(query, querynew)


def guardoContacto(contacto, numero):
    query = {"origen": numero, "contacto": contacto, "date": date, "mensajesNuevos": 0}
    collection.insert_one(query)
