from flask import request
from configuration import db
from agencyModel import addAgency, deleteAgency, selectAllAgency, selectManagerAgency, updateAgency

configs = db()


class agencyOperations:
    
    @staticmethod
    def createAgency():

        _json = request.json
        agencyname = _json['agencyname'] 
        address = _json['address']
        country = _json['country']
        town = _json['town']
        email = _json['email']
        phone = _json['phone']
        fax = _json['fax']
        manager_id = _json['manager_id']

        result = addAgency(agencyname, address, country, town, email, phone, fax, manager_id)

        return result

    @staticmethod
    def updateAgency():
        _json = request.json
        agencyname = _json['agencyname'] 
        address = _json['address']
        country = _json['country']
        town = _json['town']
        email = _json['email']
        phone = _json['phone']
        fax = _json['fax']
        manager_id = _json['manager_id']
        idA = _json['idA']

        result = updateAgency(agencyname, address, country, town, email, phone, fax, manager_id, idA)

        return result

    @staticmethod
    def deleteAgency():
        _json = request.json
        idA = _json['idA']

        result = deleteAgency(idA)

        return result

    @staticmethod
    def selectAllAgencies():
        result = selectAllAgency()
        return result

    @staticmethod
    def selectAgency():
        _json = request.json
        idA = _json['idA']
        i = _json['i']

        result = selectManagerAgency(idA, i)

        return result
