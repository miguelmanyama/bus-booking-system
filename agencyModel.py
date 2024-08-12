from flask import jsonify
from configuration import db


configs = db()

# ++++++++++ Manage Agency ++++++++++ #

def addAgency(agencyname, address, country, town, email, phone, fax, manager_id):
    
    sql = "INSERT INTO agency (agencyname, address, country, town, email, phone, fax, manager_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (agencyname, address, country, town, email, phone, fax, manager_id)

    configs[1].execute(sql, val)

    configs[2].commit()

    response = {
        "message": "Agency created successfully"
    }

    return jsonify(response)

def updateAgency(agencyname, address, country, town, email, phone, fax, manager_id, idA):

    sql = "UPDATE agency SET agencyname = %s, address = %s, country = %s, town = %s, email = %s, phone = %s, fax = %s, manager_id = %s WHERE id = %s"
    val = (agencyname, address, country, town, email, phone, fax, manager_id, idA)

    configs[1].execute(sql, val)

    configs[2].commit()

    response = {
        "message": "Agency Updated successfully"
    }

    return jsonify(response)

def deleteAgency(idA):

    sql = "DELETE FROM agency WHERE id = %s"
    val = (idA,)

    configs[1].execute(sql, val)

    configs[2].commit()

    response = {
        "message": "Agency deleted successfully"
    }

    return jsonify(response)

def selectAllAgency():

    sql = "SELECT agency.id, agency.agencyname, agency.address, agency.country, agency.town, agency.email, agency.phone, agency.fax, users.id, users.name, users.email, users.phonenumber FROM agency INNER JOIN users ON agency.manager_id = users.id"

    configs[1].execute(sql)

    result = configs[1].fetchall()

    return jsonify(result)

def selectManagerAgency(idA, i):

    sql = "SELECT agency.id, agency.agencyname, agency.address, agency.country, agency.town, agency.email, agency.phone, agency.fax, users.id, users.name, users.email, users.phonenumber FROM agency INNER JOIN users ON users.id = %s WHERE agency.id = %s"
    val = (idA, i)

    configs[1].execute(sql, val)


    result = configs[1].fetchall()

    return jsonify(result)

