from config.dbconfig import db_config
import psycopg2


class ClientsDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % (db_config['dbname'], db_config['user'],
                                                                            db_config['password'], db_config['dbport'],
                                                                            db_config['host'])
        self.conn = psycopg2.connect(connection_url)

    def get_all_clients(self):
        cursor = self.conn.cursor()
        query = "select cid, firstname, lastname, phone, company from clients;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_client_by_id(self, cid):
        cursor = self.conn.cursor()
        query = "select cid, firstname, lastname, phone, company " \
                "from clients " \
                "where cid = %s;"
        cursor.execute(query, (cid,))
        result = cursor.fetchone()
        return result

    def update_client(self, cid, firstname, lastname, phone, company):
        cursor = self.conn.cursor()
        query = "update clients " \
                "set firstname = %s, lastname = %s, phone = %s, company = %s " \
                "where cid = %s;"
        cursor.execute(query, (firstname, lastname, phone, company, cid))
        self.conn.commit()
        return True

    def delete_client(self, cid):
        cursor = self.conn.cursor()
        query = "delete from clients where cid = %s;"
        cursor.execute(query, (cid,))
        # determine affected rows
        affected_rows = cursor.rowcount
        self.conn.commit()
        # if affected rows == 0, the part was not found and hence not deleted
        # otherwise, it was deleted, so check if affected_rows != 0
        return affected_rows != 0

    def insert_client(self, firstname, lastname, phone, company):
        cursor = self.conn.cursor()
        query = "insert into clients (firstname, lastname, phone, company) " \
                "values (%s,%s,%s,%s) returning cid;"
        cursor.execute(query, (firstname, lastname, phone, company,))
        result = cursor.fetchone()[0]
        self.conn.commit()
        return result