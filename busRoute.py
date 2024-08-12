from flask import request
from configuration import db
from busModel import addBus, updateBus, deleteBus, selectAllBuses, selectBus

config = db()


class busOperations:
    
    @staticmethod
    def createBus():

        _json = request.json
        name = _json['name'] 
        typeb = _json['type']
        sits = _json['sits']
        agency_id = _json['agency_id']
        status = _json['status']

        result = addBus(name, typeb, sits, agency_id, status)

        return result

    @staticmethod
    def updateBus():
        _json = request.json
        name = _json['name'] 
        typeb = _json['type']
        sits = _json['sits']
        agency_id = _json['agency_id']
        status = _json['status']
        idB = _json['idB']

        result = updateBus(name, typeb, sits, status, agency_id, idB)

        return result

    @staticmethod
    def deleteBus():
        _json = request.json
        idB = _json['idB']

        result = deleteBus(idB)

        return result

    @staticmethod
    def selectAllBuses():
        result = selectAllBuses()
        return result
    
    @staticmethod
    def selectBus():
        _json = request.json
        idB = _json['idB']

        result = selectBus(idB)

        return result





