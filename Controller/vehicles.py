from flask import jsonify
from Model.vehicles import VehiclesDAO


class BaseVehicles:
    def build_map_dict(self, row):
        result = {}
        result['vid'] = row[0]
        result['licenseplate'] = row[1]
        result['brand'] = row[2]
        result['model'] = row[3]
        result['weight'] = row[4]
        return result

    def build_attr_dict(self, vid, licenseplate, brand, model, weight):
        result = {}
        result['vid'] = vid
        result['licenseplate'] = licenseplate
        result['brand'] = brand
        result['model'] = model
        result['weight'] = weight
        return result

    def get_all_vehicles(self):
        dao = VehiclesDAO()
        vehicles_list = dao.get_all_vehicles()
        result_list = []
        for row in vehicles_list:
            obj = self.build_map_dict(row)
            result_list.append(obj)
        return jsonify(result_list)

    def get_vehicle_by_id(self, vid):
        dao = VehiclesDAO()
        vehicle_tuple = dao.get_vehicle_by_id(vid)
        if not vehicle_tuple:
            return jsonify("Not Found"), 404
        else:
            result = self.build_map_dict(vehicle_tuple)
            return jsonify(result), 200

    def update_vehicle(self, vid, json):
        licenseplate = json['licenseplate']
        brand = json['brand']
        model = json['model']
        weight = json['weight']
        dao = VehiclesDAO()
        updated_vehicle = dao.update_vehicle(vid, licenseplate, brand, model, weight)
        result = self.build_attr_dict(vid, licenseplate, brand, model, weight)
        return jsonify(result), 200

    def delete_vehicle(self, vid):
        dao = VehiclesDAO()
        result = dao.delete_vehicle(vid)
        if result:
            return jsonify("DELETED"), 200
        else:
            return jsonify("NOT FOUND"), 404

    def add_new_vehicle(self, json):
        licenseplate = json['licenseplate']
        brand = json['brand']
        model = json['model']
        weight = json['weight']
        dao = VehiclesDAO()
        vid = dao.insert_vehicle(licenseplate, brand, model, weight)
        result = self.build_attr_dict(vid, licenseplate, brand, model, weight)
        return jsonify(result), 201
