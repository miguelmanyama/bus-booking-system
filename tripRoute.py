from flask import request
from configuration import db
from tripModel import addTrip, deleteTrip, updateTrip, selectAllTrips, selectTrip

configs = db()

class tripOperations:

    @staticmethod
    def createTrip():

        _json = request.json
        startDestination = _json['start_destination'] 
        endDestination = _json['end_destination']
        depatureTime = _json['depature_time']
        bus_id = _json['bus_id']
        agency_id = _json['agency_id']
        cost = _json['cost']

        result = addTrip(startDestination, endDestination, depatureTime, bus_id, agency_id, cost)

        return result

    @staticmethod
    def updateTrip():
        _json = request.json
        startDestination = _json['start_destination'] 
        endDestination = _json['end_destination']
        depatureTime = _json['depature_time']
        bus_id = _json['bus_id']
        agency_id = _json['agency_id']
        cost = _json['cost']
        idT = _json['idT']
        result = updateTrip(startDestination, endDestination, depatureTime, bus_id, agency_id, cost, idT)

        return result

    @staticmethod
    def deleteTrip():
        _json = request.json
        idT = _json['idT']

        result = deleteTrip(idT)

        return result

    @staticmethod
    def selectAllTrips():
        result = selectAllTrips()
        return result
    
    @staticmethod
    def selectTrip():
        _json = request.json
        idT = _json['idT']
    
        result = selectTrip(idT)

        return result




