from pymongo import MongoClient
import json

conection = MongoClient('localhost', 27017)

dataBase = conection['testdb']

collection = dataBase['Mensajes']


def realizoQuery(contacto, mensaje, hora):
    query = json.loads(
        '{"Contacto": ' + '"' + contacto + '"' + ',"Mensaje": ' + '"' + mensaje + '"' + ', "Hora": ' + '"' + hora + '"' + '}')
    result = collection.count(query)
    return result
