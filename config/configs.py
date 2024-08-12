from flask import Flask, request, jsonify
import mysql.connector

def db():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "bookinng_system"
    )

    mycursor = mydb.cursor()

    app = Flask(__name__)

    return [app, mycursor, mydb]
