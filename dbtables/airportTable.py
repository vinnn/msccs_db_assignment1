import sqlite3
from dbmodels.airport import Airport

class AirportTable:

    sql_create_if_not_exist_table = "CREATE TABLE IF NOT EXISTS airport ( \
        id INTEGER PRIMARY KEY AUTOINCREMENT, \
        name VARCHAR(20) NOT NULL, \
        city VARCHAR(20) NOT NULL, \
        country VARCHAR(20) NOT NULL, \
        weather VARCHAR(20) NOT NULL \
    );"

    ############################################# 
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

    ############################################# 
    def get_connection(self):
        self.conn = sqlite3.connect("airline.db")
        self.conn.row_factory = sqlite3.Row # to obtain query results as Row objects (that can easily be converted into dictionaries)      
        self.cur = self.conn.cursor()

    def select_all_airports(self):
        try:
            self.get_connection()
            self.cur.execute('''
                            SELECT a.id AS id, a.name AS "name", l.city AS "city", l.country AS "country"
                            FROM airport a, location l
                            WHERE a.location_id=l.id 
                             ''')
            rows = self.cur.fetchall()  # query results as list of sqlite3 Row objects
            results = [dict(row) for row in rows]   # transform query results as list of dictionaries with column names as keys
            return results

        except Exception as e:
            print(e)
        finally:
            self.conn.close()


