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
    def select_all_airports(self):
        '''
        fetch all the airports     
        '''
        try:
            self.get_connection()
            self.cur.execute('''
                            SELECT a.id AS id, a.name AS "name", a.city AS "city", a.country AS "country"
                            FROM airport a
                             ''')
            rows = self.cur.fetchall()  # query results as list of sqlite3 Row objects
            results = [dict(row) for row in rows]   # transform query results as list of dictionaries with column names as keys
            return results

        except Exception as e:
            print(e)
        finally:
            self.conn.close()

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

    ###############################################################################################################################
    def select_one_airport(self, airport_id):
        try:
            self.get_connection()
            self.cur.execute('''
                            SELECT id, name, city, country
                            FROM airport
                            WHERE id=?
                             ''',
                             (airport_id,)
                             )
            
            row = self.cur.fetchone()  # query result as sqlite3 Row object
            result = dict(row) if row is not None else None  # transform query result as dictionary with column names as keys
            return result

        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    ###############################################################################################################################
    def update_airport(self, id, field_to_update, field_new_value):

        try:
            self.get_connection()
            query = f"UPDATE airport SET {field_to_update} = ? WHERE id= ?"
            self.cur.execute(query, (field_new_value, id,))
            self.conn.commit()
            return "successful update"

        except Exception as e:
            print(e)
            return "failed update"
        finally:
            self.conn.close()

    ###############################################################################################################################
    def delete_airport(self, id):

        try:
            self.get_connection()
            query = f"DELETE FROM airport WHERE id= ?"
            self.cur.execute(query, (id,))
            self.conn.commit()
            return "successful deletion"

        except Exception as e:
            print(e)
            return "failed deletion"
        finally:
            self.conn.close()

    ###############################################################################################################################
    def create_airport(self, data):
        try:
            self.get_connection()
            query = f"INSERT INTO airport (name, city, country) VALUES (?,?,?)"
            self.cur.execute(query, 
                             (data["name"],
                              data["city"],
                              data["country"]
                              )
                            )
            self.conn.commit()
            return "successful creation"

        except Exception as e:
            print(e)
            return "failed creation"
        finally:
            self.conn.close()

