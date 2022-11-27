from config.dbconfig import db_config
import psycopg2


class UsersDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % (db_config['dbname'], db_config['user'],
                                                                            db_config['password'], db_config['dbport'],
                                                                            db_config['host'])
        self.conn = psycopg2.connect(connection_url)

    def get_all_users(self):
        cursor = self.conn.cursor()
        query = "select uid, username, useremail, userpassword, firstname, lastname from users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_user_by_id(self, uid):
        cursor = self.conn.cursor()
        query = "select uid, username, useremail, userpassword, firstname, lastname " \
                "from users " \
                "where uid = %s;"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result

    def update_user(self, uid, username, useremail, userpassword, firstname, lastname):
        cursor = self.conn.cursor()
        query = "update users " \
                "set username = %s, useremail = %s, userpassword = %s, firstname = %s, lastname = %s " \
                "where uid = %s;"
        cursor.execute(query, (username, useremail, userpassword, firstname, lastname, uid))
        self.conn.commit()
        return True

    def delete_user(self, uid):
        cursor = self.conn.cursor()
        query = "delete from users where uid = %s;"
        cursor.execute(query, (uid,))
        # determine affected rows
        affected_rows = cursor.rowcount
        self.conn.commit()
        # if affected rows == 0, the part was not found and hence not deleted
        # otherwise, it was deleted, so check if affected_rows != 0
        return affected_rows != 0

    def insert_user(self, username, useremail, userpassword, firstname, lastname):
        cursor = self.conn.cursor()
        query = "insert into users (username, useremail, userpassword, firstname, lastname) " \
                "values (%s,%s,%s,%s,%s) returning uid;"
        cursor.execute(query, (username, useremail, userpassword, firstname, lastname,))
        result = cursor.fetchone()[0]
        self.conn.commit()
        return result