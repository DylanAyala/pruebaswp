from pymongo import MongoClient
from datetime import datetime
import json

conection = MongoClient('localhost', 27017)

dataBase = conection['testdb']

collection = dataBase['MensajesBulk']


def hayMensajesNuevos(numero):
    query = json.loads(
        '{"procesado": 0, "origen": "' + numero + '"}')
    resultado = collection.count(query)
    return resultado


def buscoMensajesNuevos(numero):
    query = json.loads(
        '{"procesado": 0, "origen": "' + numero + '"}')
    result = collection.find(query)

    return result


def actualizoMensajeEnviado(contacto, mensaje, numero):
    query = json.loads(
        '{"origen": "' + numero + '","contacto": ' + '"' + contacto + '"' + ',"mensaje": ' + '"' + mensaje + '"' + ', "procesado": 0}')
    newQuery = json.loads('{"$set": {"procesado": 1}}')
    collection.update_one(query, newQuery)
