from flask import jsonify
from Model.users import UsersDAO


class BaseUsers:
    def build_map_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['username'] = row[1]
        result['useremail'] = row[2]
        result['userpassword'] = row[3]
        result['firstname'] = row[4]
        result['lastname'] = row[5]
        return result

    def build_attr_dict(self, uid, username, useremail, userpassword, firstname, lastname):
        result = {}
        result['uid'] = uid
        result['username'] = username
        result['useremail'] = useremail
        result['userpassword'] = userpassword
        result['firstname'] = firstname
        result['lastname'] = lastname
        return result

    def get_all_users(self):
        dao = UsersDAO()
        user_list = dao.get_all_users()
        result_list = []
        for row in user_list:
            obj = self.build_map_dict(row)
            result_list.append(obj)
        return jsonify(result_list)

    def get_user_by_id(self, uid):
        dao = UsersDAO()
        user_tuple = dao.get_user_by_id(uid)
        if not user_tuple:
            return jsonify("Not Found"), 404
        else:
            result = self.build_map_dict(user_tuple)
            return jsonify(result), 200

    def update_user(self, uid, json):
        username = json['username']
        useremail = json['useremail']
        userpassword = json['userpassword']
        firstname = json['firstname']
        lastname = json['lastname']
        dao = UsersDAO()
        updated_user = dao.update_user(uid, username, useremail, userpassword, firstname, lastname)
        result = self.build_attr_dict(uid, username, useremail, userpassword, firstname, lastname)
        return jsonify(result), 200

    def delete_user(self, uid):
        dao = UsersDAO()
        result = dao.delete_user(uid)
        if result:
            return jsonify("DELETED"), 200
        else:
            return jsonify("NOT FOUND"), 404

    def add_new_user(self, json):
        username = json['username']
        useremail = json['useremail']
        userpassword = json['userpassword']
        firstname = json['firstname']
        lastname = json['lastname']
        dao = UsersDAO()
        uid = dao.insert_user(username, useremail, userpassword, firstname, lastname)
        result = self.build_attr_dict(uid, username, useremail, userpassword, firstname, lastname)
        return jsonify(result), 201
