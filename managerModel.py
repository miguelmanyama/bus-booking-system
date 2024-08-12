from flask import jsonify
from configuration import db    

configs = db()


def addManager(name, email, phonenumber, password):
    sql = "INSERT INTO users (name, email, phonenumber, password, role) VALUES (%s, %s, %s, %s, 'manager')"
    val = (name, email, phonenumber, password)

    configs[1]  
    configs[2].commit()

    response = {
        "message": "Manager created successfully"
    }

    return jsonify(response)

def updateManager(name, email, phonenumber, password, idM):
    sql = "UPDATE users SET name = %s, email = %s, phonenumber = %s, password = %s WHERE id = %s"
    val = (name, email, phonenumber, password, idM)

    configs[1].execute(sql, val)
    configs[2].commit()

    response = {
        "message": "Manager updated successfully"
    }

    return jsonify(response)

def deleteManager(idM):
    sql = "DELETE FROM users WHERE id = %s"
    val = (idM,)

    configs[1].execute(sql, val)
    configs[2].commit()

    response = {
        "message": "Manager deleted successfully"
    }

    return jsonify(response)

def selectManager():
    sql = "SELECT * from users WHERE role = 'manager'"

    configs[1].execute(sql)
    result = configs[1].fetchall()

    return jsonify(result)