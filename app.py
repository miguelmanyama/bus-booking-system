from flask import Flask, jsonify, request
from agencyRoute import agencyOperations
from bookingRoute import bookingOperations
from busRoute import busOperations
from managerRoute import ManagerOperations
from tripRoute import tripOperations

app = Flask(__name__)
    # ========== AGENCY ROUTES ========== #
@app.route('/createAgency', methods=['POST'])
def create_agency():
   result = agencyOperations.createAgency()
   return result

@app.route('/updateAgency', methods=['put'])
def update_agency():
    result = agencyOperations.updateAgency()
    return result

@app.route('/deleteAgency', methods=['delete'])
def delete_agency():
    result = agencyOperations.deleteAgency()
    return result

@app.route('/selectAllAgencies', methods=['get'])
def select_all_agencies():
    result = agencyOperations.selectAllAgencies()
    return result

@app.route('/selectAgency', methods=['get'])
def select_agency():
    result = agencyOperations.selectAgency()
    return result


    # ========== BOOKING ROUTES ========== #
@app.route('/addBooking', methods=['POST'])
def create_booking():
    result = bookingOperations.createBooking()
    return result 

@app.route('/updateBooking', methods=['put'])
def update_booking():
    result = bookingOperations.updateBooking()
    return result

@app.route('/deleteBooking', methods=['delete'])
def delete_booking():
    result = bookingOperations.deleteBooking()
    return result

@app.route('/selectAllBooking', methods=['get'])
def select_all_booking():
    result = bookingOperations.selectAllBookings()
    return result 


    # ========== BUS ROUTES ========== #

@app.route('/addBus', methods=['POST'])
def create_bus():
    result = busOperations.createBus()
    return result

@app.route('/updateBus', methods=['put'])
def update_bus():
    result = busOperations.updateBus()
    return result

@app.route('/deleteBus', methods=['delete'])
def delete_bus():
   result = busOperations.deleteBus()
   return result

@app.route('/selectAllBuses', methods=['get'])
def select_all_buses():
    result = busOperations.selectAllBuses()
    return result

@app.route('/selectBus', methods=['get'])
def select_bus():
    result = busOperations.selectBus()
    return result


    # ========== MANAGER ROUTES ========== #

@app.route('/createManager', methods=['POST'])
def create_manager():
    result = ManagerOperations.createManager()
    return result

@app.route('/updateManager', methods=['PUT'])
def update_manager():
    result = ManagerOperations.updateManager()
    return result

@app.route('/deleteManager', methods=['DELETE'])
def delete_manager():
    result = ManagerOperations.deleteManager()
    return result

@app.route('/selectManager', methods=['GET'])
def select_manager():
    result = ManagerOperations.selectManager()
    return result

    # ========== TRIPS ROUTES ========== #


@app.route('/createTrip', methods = ['POST'])
def create_trip():
    result = tripOperations.createTrip()
    return result

@app.route('/updateTrip', methods = ['put'])
def update_trip():
    result = tripOperations.updateTrip()
    return result
   
@app.route('/deleteTrip', methods = ['DELETE'])
def delete_trip():
    result = tripOperations.deleteTrip()
    return result

@app.route('/selectAllTrips', methods = ['GET'])
def select_all_trip():
    result = tripOperations.selectAllTrips()
    return result

@app.route('/selectTrip', methods = ['GET'])
def select_trip():
    result = tripOperations.selectTrip()
    return result
   
   
   
if __name__ == "__main__":
    app.run()