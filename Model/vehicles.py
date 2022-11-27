from config.dbconfig import db_config
import psycopg2


class VehiclesDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % (db_config['dbname'], db_config['user'],
                                                                            db_config['password'], db_config['dbport'],
                                                                            db_config['host'])
        self.conn = psycopg2.connect(connection_url)

    def get_all_vehicles(self):
        cursor = self.conn.cursor()
        query = "select vid, licenseplate, brand, model, weight from vehicles;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_vehicle_by_id(self, vid):
        cursor = self.conn.cursor()
        query = "select vid, licenseplate, brand, model, weight " \
                "from vehicles " \
                "where vid = %s;"
        cursor.execute(query, (vid,))
        result = cursor.fetchone()
        return result

    def update_vehicle(self, vid, licenseplate, brand, model, weight):
        cursor = self.conn.cursor()
        query = "update vehicles " \
                "set licenseplate = %s, brand = %s, model = %s, weight = %s " \
                "where vid = %s;"
        cursor.execute(query, (licenseplate, brand, model, weight, vid))
        self.conn.commit()
        return True

    def delete_vehicle(self, vid):
        cursor = self.conn.cursor()
        query = "delete from vehicles where vid = %s;"
        cursor.execute(query, (vid,))
        # determine affected rows
        affected_rows = cursor.rowcount
        self.conn.commit()
        # if affected rows == 0, the part was not found and hence not deleted
        # otherwise, it was deleted, so check if affected_rows != 0
        return affected_rows != 0

    def insert_vehicle(self, licenseplate, brand, model, weight):
        cursor = self.conn.cursor()
        query = "insert into vehicles (licenseplate, brand, model, weight) " \
                "values (%s,%s,%s,%s) returning vid;"
        cursor.execute(query, (licenseplate, brand, model, weight,))
        result = cursor.fetchone()[0]
        self.conn.commit()
        return result