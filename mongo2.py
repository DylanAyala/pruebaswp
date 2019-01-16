from pymongo import MongoClient
from datetime import datetime
import json

conection = MongoClient('localhost', 27017)

dataBase = conection['testdb']

collection = dataBase['Mensajes']

mensaje = 'Jsbsbz'
hora = '15:48'


def armoQuery(mensaje, hora):
    query = {"Mensaje": '"' + mensaje + '"', "Hora": '"' + hora + '"'}
    return query



query = json.loads('{"Mensaje": ' + '"' + mensaje + '"' + ', "Hora": ' + '"' + hora + '"' + '}')


def realizoQuery():
    result = collection.find(query)
    for x in result:
        print(x['Mensaje'])


print(query)

realizoQuery()
