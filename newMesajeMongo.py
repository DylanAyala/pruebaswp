from pymongo import MongoClient
from datetime import datetime
import json

conection = MongoClient('localhost', 27017)

dataBase = conection['testdb']

collection = dataBase['MensajesBulk']


def hayMensajesNuevos():
    query = json.loads(
        '{"Procesado": "0"}')
    resultado = collection.count(query)
    return resultado


def buscoMensajesNuevos():
    query = json.loads(
        '{"Procesado": "0"}')
    result = collection.find(query)

    return result


def actualizoMensajeEnviado(contacto, mensaje):
    query = json.loads(
        '{"Contacto": ' + '"' + contacto + '"' + ',"Mensaje": ' + '"' + mensaje + '"' + ', "Procesado": "0"}')
    newQuery = json.loads('{"$set": {"Procesado": "1"}}')
    collection.update_one(query, newQuery)
