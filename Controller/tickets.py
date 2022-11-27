from flask import jsonify
from Model.tickets import TicketsDAO


class BaseTickets:
    def build_map_dict(self, row):
        result = {}
        result['tid'] = row[0]
        result['vid'] = row[1]
        result['model'] = row[2]
        result['brand'] = row[3]
        result['firstname'] = row[4]
        result['lastname'] = row[5]
        result['company'] = row[6]
        result['material'] = row[7]
        result['measurementtype'] = row[8]
        result['measurement'] = row[9]
        result['cost'] = row[10]
        return result

    def build_attr_dict(self, tid, vid, model, brand, firstname, lastname, company, material, measurementtype, measurement, cost):
        result = {}
        result['tid'] = tid
        result['vid'] = vid
        result['model'] = model
        result['brand'] = brand
        result['firstname'] = firstname
        result['lastname'] = lastname
        result['company'] = company
        result['material'] = material
        result['measurementtype'] = measurementtype
        result['measurement'] = measurement
        result['cost'] = cost
        return result

    def get_all_tickets(self):
        dao = TicketsDAO()
        ticket_list = dao.get_all_tickets()
        result_list = []
        for row in ticket_list:
            obj = self.build_map_dict(row)
            result_list.append(obj)
        return jsonify(result_list)

    def get_ticket_by_id(self, tid):
        dao = TicketsDAO()
        ticket_tuple = dao.get_ticket_by_id(tid)
        if not ticket_tuple:
            return jsonify("Not Found"), 404
        else:
            result = self.build_map_dict(ticket_tuple)
            return jsonify(result), 200

    def update_ticket(self, tid, json):
        vid = json['vid']
        model = json['model']
        brand = json['brand']
        firstname = json['firstname']
        lastname = json['lastname']
        company = json['company']
        material = json['material']
        measurementtype = json['measurementtype']
        measurement = json['measurement']
        cost = json['cost']
        dao = TicketsDAO()
        updated_ticket = dao.update_ticket(tid, vid, model, brand, firstname, lastname, company, material, measurementtype, measurement, cost)
        result = self.build_attr_dict(tid, vid, model, brand, firstname, lastname, company, material, measurementtype, measurement, cost)
        return jsonify(result), 200

    def delete_ticket(self, tid):
        dao = TicketsDAO()
        result = dao.delete_ticket(tid)
        if result:
            return jsonify("DELETED"), 200
        else:
            return jsonify("NOT FOUND"), 404

    def add_new_ticket(self, json):
        vid = json['vid']
        model = json['model']
        brand = json['brand']
        firstname = json['firstname']
        lastname = json['lastname']
        company = json['company']
        material = json['material']
        measurementtype = json['measurementtype']
        measurement = json['measurement']
        cost = json['cost']
        dao = TicketsDAO()
        tid = dao.insert_ticket(vid, model, brand, firstname, lastname, company, material, measurementtype, measurement, cost)
        result = self.build_attr_dict(tid, vid, model, brand, firstname, lastname, company, material, measurementtype, measurement, cost)
        return jsonify(result), 201
