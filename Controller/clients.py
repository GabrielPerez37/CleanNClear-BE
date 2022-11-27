from flask import jsonify
from Model.clients import ClientsDAO


class BaseClients:
    def build_map_dict(self, row):
        result = {}
        result['cid'] = row[0]
        result['firstname'] = row[1]
        result['lastname'] = row[2]
        result['phone'] = row[3]
        result['company'] = row[4]
        return result

    def build_attr_dict(self, cid, firstname, lastname, phone, company):
        result = {}
        result['cid'] = cid
        result['firstname'] = firstname
        result['lastname'] = lastname
        result['phone'] = phone
        result['company'] = company
        return result

    def get_all_clients(self):
        dao = ClientsDAO()
        client_list = dao.get_all_clients()
        result_list = []
        for row in client_list:
            obj = self.build_map_dict(row)
            result_list.append(obj)
        return jsonify(result_list)

    def get_client_by_id(self, cid):
        dao = ClientsDAO()
        client_tuple = dao.get_client_by_id(cid)
        if not client_tuple:
            return jsonify("Not Found"), 404
        else:
            result = self.build_map_dict(client_tuple)
            return jsonify(result), 200

    def update_client(self, cid, json):
        firstname = json['firstname']
        lastname = json['lastname']
        phone = json['phone']
        company = json['company']
        dao = ClientsDAO()
        updated_client = dao.update_client(cid, firstname, lastname, phone, company)
        result = self.build_attr_dict(cid, firstname, lastname, phone, company)
        return jsonify(result), 200

    def delete_client(self, cid):
        dao = ClientsDAO()
        result = dao.delete_client(cid)
        if result:
            return jsonify("DELETED"), 200
        else:
            return jsonify("NOT FOUND"), 404

    def add_new_client(self, json):
        firstname = json['firstname']
        lastname = json['lastname']
        phone = json['phone']
        company = json['company']
        dao = ClientsDAO()
        cid = dao.insert_client(firstname, lastname, phone, company)
        result = self.build_attr_dict(cid, firstname, lastname, phone, company)
        return jsonify(result), 201
