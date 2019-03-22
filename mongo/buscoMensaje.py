from pymongo import MongoClient
import json

conection = MongoClient('localhost', 27017)

dataBase = conection['testdb']

collection = dataBase['Mensajes']


def realizoQuery(contacto, mensaje, hora, numero):
    query = json.loads(
        '{"origen": "' + numero + '","contacto": ' + '"' + contacto + '"' + ',"mensaje": ' + '"' + mensaje + '"' + ', "hora": ' + '"' + hora + '"' + '}')
    result = collection.count(query)
    return result
