from flask import request
from configuration import db
from managerModel import addManager, updateManager, deleteManager, selectManager

config = db()

class ManagerOperations:
    @staticmethod       
    def createManager():
        _json = request.json
        name = _json['name'] 
        email = _json['email']
        phonenumber = _json['phonenumber']
        password = _json['password']

        result = addManager(name, email, phonenumber, password)
        return result

    @staticmethod
    def updateManager():
        _json = request.json
        name = _json['name'] 
        email = _json['email']
        phonenumber = _json['phonenumber']
        password = _json['password']
        idM = _json['idM']

        result = updateManager(name, email, phonenumber, password, idM)
        return result

    @staticmethod
    def deleteManager():
        _json = request.json
        idM = _json['idM']

        result = deleteManager(idM)
        return result

    @staticmethod
    def selectManager():
        result = selectManager()
        return result