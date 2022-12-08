from flask import Flask, request, jsonify
from flask_cors import CORS

from Controller.users import BaseUsers
from Controller.clients import BaseClients
from Controller.vehicles import BaseVehicles
from Controller.tickets import BaseTickets


app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Welcome To Clean \'N Clear'


@app.route('/CleanNClear/users', methods=['GET', 'POST'])
def handle_users():
    if request.method == 'POST':
        return BaseUsers().add_new_user(request.json)
    else:
        return BaseUsers().get_all_users()


@app.route('/CleanNClear/users/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def handle_users_by_id(uid):
    if request.method == 'GET':
        return BaseUsers().get_user_by_id(uid)
    elif request.method == 'PUT':
        return BaseUsers().update_user(uid, request.json)
    elif request.method == 'DELETE':
        return BaseUsers().delete_user(uid)
    else:
        return jsonify("Method Not Allowed"), 405


@app.route('/CleanNClear/vehicles', methods=['GET', 'POST'])
def handle_vehicles():
    if request.method == 'POST':
        return BaseVehicles().add_new_vehicle(request.json)
    else:
        return BaseVehicles().get_all_vehicles()


@app.route('/CleanNClear/vehicles/<int:vid>', methods=['GET', 'PUT', 'DELETE'])
def handle_vehicles_by_id(vid):
    if request.method == 'GET':
        return BaseVehicles().get_vehicle_by_id(vid)
    elif request.method == 'PUT':
        return BaseVehicles().update_vehicle(vid, request.json)
    elif request.method == 'DELETE':
        return BaseVehicles().delete_vehicle(vid)
    else:
        return jsonify("Method Not Allowed"), 405


@app.route('/CleanNClear/clients', methods=['GET', 'POST'])
def handle_clients():
    if request.method == 'POST':
        return BaseClients().add_new_client(request.json)
    else:
        return BaseClients().get_all_clients()


@app.route('/CleanNClear/clients/<int:cid>', methods=['GET', 'PUT', 'DELETE'])
def handle_clients_by_id(cid):
    if request.method == 'GET':
        return BaseClients().get_client_by_id(cid)
    elif request.method == 'PUT':
        return BaseClients().update_client(cid, request.json)
    elif request.method == 'DELETE':
        return BaseClients().delete_client(cid)
    else:
        return jsonify("Method Not Allowed"), 405


@app.route('/CleanNClear/tickets', methods=['GET', 'POST'])
def handle_tickets():
    if request.method == 'POST':
        return BaseTickets().add_new_ticket(request.json)
    else:
        return BaseTickets().get_all_tickets()


@app.route('/CleanNClear/tickets/<int:tid>', methods=['GET', 'PUT', 'DELETE'])
def handle_tickets_by_id(tid):
    if request.method == 'GET':
        return BaseTickets().get_ticket_by_id(tid)
    elif request.method == 'PUT':
        return BaseTickets().update_ticket(tid, request.json)
    elif request.method == 'DELETE':
        return BaseTickets().delete_ticket(tid)
    else:
        return jsonify("Method Not Allowed"), 405


if __name__ == '__main__':
    app.run()
