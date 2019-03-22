from pymongo import MongoClient
import json
from datetime import datetime

conection = MongoClient('localhost', 27017)

dataBase = conection['testdb']

collection = dataBase['Contactos']


def buscoContactoConMensajesCount(numero):
    query = json.loads('{"mensajesNuevos": 0, "origen": "' + numero + '"}')
    count = collection.count(query)
    return count


def buscoContactoConMensajes(numero):
    query = json.loads('{"mensajesNuevos": 0, "origen": "' + numero + '"}')
    resultado = collection.find(query)
    return resultado


def actualizoContacto(contacto, numero):
    query = json.loads('{"contacto": "' + contacto + '", "origen": "' + numero + '"}')
    querynew = json.loads('{"$set": {"contacto": "' + contacto + '","mensajesNuevos": 1}}')
    collection.update_one(query, querynew)
