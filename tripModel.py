from flask import jsonify
from configuration import db


configs = db()
# ++++++++++ Manage trip ++++++++++ #

def addTrip(startDestination, endDestination, depatureTime, bus_id, agency_id, cost):

    sql = "INSERT INTO trip (start_destination, end_destination, departure_time, bus_id, agency_id, cost) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (startDestination, endDestination, depatureTime, bus_id, agency_id, cost)

    configs[1].execute(sql, val)

    configs[2].commit()

    response = {
        "message": "Trip created successfully"
    }

    return jsonify(response)

def updateTrip(startDestination, endDestination, depatureTime, bus_id, agency_id, cost, idT):

    sql = "UPDATE trip SET start_destination = %s , end_destination = %s, departure_time = %s, bus_id = %s, agency_id = %s, cost = %s WHERE id = %s"
    val = (startDestination, endDestination, depatureTime, bus_id, agency_id, cost, idT)

    configs[1].execute(sql, val)

    configs[2].commit()

    response = {
        "message": "Trip updated successfully"
    }

    return jsonify(response)

def deleteTrip(idT):

    sql = "DELETE FROM trip WHERE id = %s"
    val = (idT,)

    configs[1].execute(sql, val)

    configs[2].commit()

    response = {
        "message": "Trip deleted successfully"
    }

    return jsonify(response)

def selectAllTrips():

    sql = "SELECT trip.id, trip.start_destination, trip.end_destination, trip.departure_time, bus.id, bus.name, bus.type, bus.sits, bus.status, agency.id, agency.agencyname, agency.address, agency.country, agency.town, agency.email, agency.phone, agency.fax FROM ((trip INNER JOIN bus ON trip.bus_id = bus.id) INNER JOIN agency ON trip.agency_id = agency.id)"

    configs[1].execute(sql)

    result = configs[1].fetchall()

    return jsonify(result)

def selectTrip(idT):

    sql = "SELECT trip.id, trip.start_destination, trip.end_destination, trip.departure_time, bus.id, bus.name, bus.type, bus.sits, bus.status, agency.id, agency.agencyname, agency.address, agency.country, agency.town, agency.email, agency.phone, agency.fax FROM ((trip INNER JOIN bus ON trip.bus_id = bus.id) INNER JOIN agency ON trip.agency_id = agency.id) WHERE trip.id = %s"
    val = (idT,)

    configs[1].execute(sql, val)
    result = configs[1].fetchall()

    return jsonify(result)
