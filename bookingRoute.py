from flask import request
from configuration import db
from bookingModel import addBooking, selectAllBookings, deleteBooking, updateBooking

config = db()


class bookingOperations:
    
    @staticmethod
    def createBooking():

        _json = request.json
        client_id = _json['client_id'] 
        bus_id = _json['bus_id']
        trip_id = _json['trip_id']
        status = _json['status']
        date = _json['date']

        result = addBooking(client_id, bus_id, trip_id, status, date)

        return result

    @staticmethod
    def updateBooking():
        _json = request.json
        client_id = _json['client_id'] 
        bus_id = _json['bus_id']
        trip_id = _json['trip_id']
        status = _json['status']
        date = _json['date']
        idBK = _json['idBK']

        result = updateBooking(client_id, bus_id, trip_id, status, date, idBK)

        return result

    @staticmethod
    def deleteBooking():
        _json = request.json
        idBK = _json['idBK']

        result = deleteBooking(idBK)

        return result

    @staticmethod
    def selectAllBookings():
        result = selectAllBookings()
        return result




