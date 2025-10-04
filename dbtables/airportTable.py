import sqlite3

class AirportTable:

    sql_create_if_not_exist_table = "CREATE TABLE IF NOT EXISTS airport ( \
        id INTEGER PRIMARY KEY AUTOINCREMENT, \
        name VARCHAR(20) NOT NULL, \
        city VARCHAR(20) NOT NULL, \
        country VARCHAR(20) NOT NULL, \
        weather VARCHAR(20) NOT NULL \
    );"

    ###############################################################################################################################
    def __init__(self):
        try:
            self.conn = sqlite3.connect("airline.db")
            self.cur = self.conn.cursor()
            self.cur.execute(self.sql_create_if_not_exist_table)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    ###############################################################################################################################
    def get_connection(self):
        self.conn = sqlite3.connect("airline.db")
        self.conn.row_factory = sqlite3.Row # to obtain query results as Row objects (that can easily be converted into dictionaries)      
        self.cur = self.conn.cursor()

    ###############################################################################################################################
    def select_all_departure_airports(self):
        '''
        fetch all the airports from where at least one flight is departing
        (for all future flights)        
        '''
        try:
            self.get_connection()
            self.cur.execute('''
                            SELECT a.id AS id, a.name AS "name", a.city AS "city", a.country AS "country"
                            FROM airport a
                            WHERE id
                            IN (
                                SELECT f.departure_airport_id
                                FROM flight f
                                WHERE f.departure_datetime > datetime('now', 'localtime')
                            )
                             ''')
            rows = self.cur.fetchall()  # query results as list of sqlite3 Row objects
            results = [dict(row) for row in rows]   # transform query results as list of dictionaries with column names as keys
            return results

        except Exception as e:
            print(e)
        finally:
            self.conn.close()


    ###############################################################################################################################
    def select_all_arrival_airports(self):
        '''
        fetch all the airports to where at least one flight is arriving
        (for all future flights)
        '''
        try:
            self.get_connection()
            self.cur.execute('''
                            SELECT a.id AS id, a.name AS "name", a.city AS "city", a.country AS "country"
                            FROM airport a
                            WHERE id
                            IN (
                                SELECT f.arrival_airport_id
                                FROM flight f
                                WHERE f.departure_datetime > datetime('now', 'localtime')
                            )
                             ''')
            rows = self.cur.fetchall()  # query results as list of sqlite3 Row objects
            results = [dict(row) for row in rows]   # transform query results as list of dictionaries with column names as keys
            return results

        except Exception as e:
            print(e)
        finally:
            self.conn.close()
