from pymongo import MongoClient
import json
from datetime import datetime

conection = MongoClient('localhost', 27017)

dataBase = conection['testdb']

collection = dataBase['Contactos']

date = datetime.now()


def guardoContacto(contacto):
    query = {"Contacto": contacto, "MensajesNuevos": 0, "date": date}
    collection.insert_one(query)