from config.dbconfig import db_config
import psycopg2


class TicketsDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % (db_config['dbname'], db_config['user'],
                                                                            db_config['password'], db_config['dbport'],
                                                                            db_config['host'])
        self.conn = psycopg2.connect(connection_url)

    def get_all_tickets(self):
        cursor = self.conn.cursor()
        query = "select tid, username, useremail, userpassword, firstname, lastname from users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_ticket_by_id(self, tid):
        cursor = self.conn.cursor()
        query = "select tid, vid, model, brand, firstname, lastname, company, material, measurementtype, measurement, cost " \
                "from tickets " \
                "where tid = %s;"
        cursor.execute(query, (tid,))
        result = cursor.fetchone()
        return result

    def update_ticket(self, tid, vid, model, brand, firstname, lastname, company, material, measurementtype, measurement, cost):
        cursor = self.conn.cursor()
        query = "update tickets " \
                "set vid = %s, model = %s, brand = %s, firstname = %s, lastname = %s, company = %s, material = %s, measurementtype = %s, measurement = %s, cost = %s" \
                "where uid = %s;"
        cursor.execute(query, (vid, model, brand, firstname, lastname, company, material, measurementtype, measurement, cost, tid))
        self.conn.commit()
        return True

    def delete_ticket(self, tid):
        cursor = self.conn.cursor()
        query = "delete from tickets where tid = %s;"
        cursor.execute(query, (tid,))
        # determine affected rows
        affected_rows = cursor.rowcount
        self.conn.commit()
        # if affected rows == 0, the part was not found and hence not deleted
        # otherwise, it was deleted, so check if affected_rows != 0
        return affected_rows != 0

    def insert_ticket(self, vid, model, brand, firstname, lastname, company, material, measurementtype, measurement, cost):
        cursor = self.conn.cursor()
        query = "insert into tickets (vid, model, brand, firstname, lastname, company, material, measurementtype, measurement, cost) " \
                "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) returning tid;"
        cursor.execute(query, (vid, model, brand, firstname, lastname, company, material, measurementtype, measurement, cost,))
        result = cursor.fetchone()[0]
        self.conn.commit()
        return result