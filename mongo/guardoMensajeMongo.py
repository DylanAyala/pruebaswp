from pymongo import MongoClient
from datetime import datetime

conection = MongoClient('localhost', 27017)

dataBase = conection['testdb']

collection = dataBase['Mensajes']

horaLeido = datetime.now()


def insert(contacto, mensaje, hora, numero):
    mydict = {"origen": numero, "contacto": contacto, "mensaje": mensaje, "hora": hora, "horaLeido": horaLeido}
    collection.insert_one(mydict)
