from flask import jsonify
from configuration import db


configs = db()
# ++++++++++ Manage Booking ++++++++++ #

def addBooking(client_id, bus_id, trip_id, status, date):

    sql = "INSERT INTO booking (client_id, bus_id, trip_id, status, date) VALUES (%s, %s, %s, %s, %s)"
    val = (client_id, bus_id, trip_id, status, date)

    configs[1].execute(sql, val)

    configs[2].commit()

    response = {
        "message": "Booking created successfully"
    }

    return jsonify(response)

def updateBooking(client_id, bus_id, trip_id, status, date, idBK):

    sql = "UPDATE booking SET client_id = %s, bus_id = %s, trip_id = %s, status = %s, date = %s WHERE id = %s"
    val = (client_id, bus_id, trip_id, status, date, idBK)

    configs[1].execute(sql, val)

    configs[2].commit()

    response = {
        "message": "Booking updated successfully"
    }

    return jsonify(response)

def deleteBooking(idBK):

    sql = "DELETE FROM booking WHERE id = %s"
    val = (idBK,)

    configs[1].execute(sql, val)

    configs[2].commit()

    response = {
        "message": "Booking deleted successfully"
    }

    return jsonify(response)

def selectAllBookings():

    sql = "SELECT booking.id, booking.status, booking.date, bus.id, bus.name, bus.type, bus.sits, trip.id, trip.start_destination, trip.end_destination, trip.departure_time, users.id, users.name, users.phonenumber From (((booking INNER JOIN users ON booking.client_id = users.id) INNER JOIN bus ON booking.bus_id = bus.id) INNER JOIN trip ON booking.trip_id = trip.id) "

    configs[1].execute(sql)

    result = configs[1].fetchall()

    return jsonify(result)
