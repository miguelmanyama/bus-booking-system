from flask import jsonify
from configuration import db


configs = db()
# +++++++++ Manage Bus ++++++++++ #

def addBus(name, typeb, sits, agency_id, status):

    sql = "INSERT INTO bus (name, type, sits, agency_id, status) VALUES (%s, %s, %s, %s, %s)"
    val = (name, typeb, sits, agency_id, status)

    configs[1].execute(sql, val)

    configs[2].commit()

    response = {
        "message": "Bus created successfully"
    }

    return jsonify(response)

def updateBus(name, typeb, sits, status, agency_id, idB):

    sql = "UPDATE bus SET name = %s, type = %s, sits = %s, status = %s, agency_id = %s WHERE id = %s"
    val = (name, typeb, sits, status, agency_id, idB)

    configs[1].execute(sql, val)

    configs[2].commit()

    response = {
        "message": "Bus updated successfully"
    }

    return jsonify(response)

def deleteBus(idB):

    sql = "UPDATE bus SET status = 'Inactive' WHERE id = %s"
    val = (idB,) 

    configs[1].execute(sql, val)

    configs[2].commit()

    response = {
        "message": "Bus disabled successfully"
    }

    return jsonify(response)

def selectAllBuses():

    sql = "SELECT bus.id, bus.name, bus.type, bus.sits, bus.status, agency.id, agency.agencyname, agency.address, agency.country, agency.town, agency.email, agency.phone FROM bus INNER JOIN agency ON bus.agency_id = agency.id"

    configs[1].execute(sql)
    result = configs[1].fetchall()

    return jsonify(result)

def selectBus(idB):

    sql = "SELECT bus.id, bus.name, bus.type, bus.sits, bus.status, agency.id, agency.agencyname, agency.address, agency.country, agency.town, agency.email, agency.phone FROM bus INNER JOIN agency ON  bus.agency_id = agency.id WHERE bus.id = %s"
    val = (idB,)

    configs[1].execute(sql, val)

    result = configs[1].fetchall()

    return jsonify(result)