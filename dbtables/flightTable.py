import sqlite3
from dbmodels.flight import Flight
from dbtables.airportTable import AirportTable
from dbtables.pilotTable import PilotTable




class FlightTable:

    sql_create_if_not_exist_table = "CREATE TABLE IF NOT EXISTS flight ( \
        id INTEGER PRIMARY KEY AUTOINCREMENT, \
        routeId VARCHAR(10) NOT NULL REFERENCES route(id), \
        statusId INTEGER NOT NULL REFERENCES status(id), \
        pilotId INTEGER NOT NULL REFERENCES pilot(id), \
        departureDate DATE NOT NULL, \
        departureTime TIME NOT NULL \
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
    def insert_new_flight(self):   #TODO: refresh this
        try:
            flight = Flight()

            # show route information (including ids) in order to create new flight
            airportTable = AirportTable()
            airportTable.select_all_airports()

            flight.set_departure_airport_id(input("Enter departure airport id: "))
            flight.set_destination_airport_id(input("Enter destination airport id: "))

            flight.set_departure_date(input("Enter flight detaprture date (YR-MM-DD): "))
            flight.set_departure_time(input("Enter flight detaprture time (HR:MM:SS): "))

            # show pilot information (including ids) in order to create new flight
            pliotTable = PilotTable()
            pliotTable.select_all_pilots()

            flight.set_pilotId(input("Enter flight pilot id: "))

            self.get_connection()
            sql_insert = "INSERT INTO flight (departure_airport_id, destination_airport_id, status_id, pilot_id, departure_date, departure_time) VALUES (?,?,?,?,?,?)"
            self.cur.execute(sql_insert, tuple(str(flight).split("\n")))

            confirm = True if input("confirm creation (Y/N): ") == "Y" else False
            if confirm:
                self.conn.commit()
                print("Inserted data successfully")
            else:
                print("Cancelled insertion")

        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    ###############################################################################################################################
    def select_all_future_flights(self):
        try:
            self.get_connection()
            self.cur.execute('''
                            SELECT f.id AS id, f.departure_date AS "departure_date", f.departure_time AS "departure_time", 
                             a1.name AS "departure_airport", l1.city AS "departure_city", l1.country AS "departure_country", 
                             a2.name AS "destination_airport", l2.city AS "destination_city", l2.country AS "destination_country", 
                             s.text AS "status" 
                            FROM flight f, airport a1, airport a2, status s, location l1, location l2
                            WHERE 
                             f.departure_airport_id=a1.id 
                             AND f.destination_airport_id=a2.id 
                             AND f.status_id=s.id 
                             AND a1.location_id=l1.id 
                             AND a2.location_id=l2.id
                             AND datetime(f.departure_date || ' ' || f.departure_time) >= datetime('now')                          
                             ORDER BY f.departure_date, f.departure_time ASC
                             ''')
            rows = self.cur.fetchall()  # query results as list of sqlite3 Row objects
            results = [dict(row) for row in rows]   # transform query results as list of dictionaries with column names as keys
            return results

        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    ###############################################################################################################################
    def select_one_flight(self, flight_id):
        try:
            self.get_connection()
            # LEFT JOIN for pilot IN ORDER TO SHOW RESULTS EVEN IF NO PILOT ASSIGNED OR MATCHING
            self.cur.execute('''
                            SELECT f.id AS id, f.departure_date AS "departure_date", f.departure_time AS "departure_time", 
                             a1.name AS "departure_airport", l1.city AS "departure_city", l1.country AS "departure_country", 
                             a2.name AS "destination_airport", l2.city AS "destination_city", l2.country AS "destination_country", 
                             s.text AS "status", 
                             p.id AS "pilot_id", p.first_name AS "pilot_first_name", p.last_name AS "pilot_last_name" 
                            FROM flight f, airport a1, airport a2, status s, location l1, location l2
                             LEFT JOIN pilot p ON f.pilot_id=p.id
                            WHERE
                             f.id=?
                             AND f.departure_airport_id=a1.id 
                             AND f.destination_airport_id=a2.id 
                             AND f.status_id=s.id 
                             AND a1.location_id=l1.id 
                             AND a2.location_id=l2.id
                             ''',
                             (flight_id,)
                             )
            
            row = self.cur.fetchone()  # query result as sqlite3 Row object
            result = dict(row) if row is not None else None  # transform query result as dictionary with column names as keys
            return result

        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    ###############################################################################################################################
    def select_flights_by_departure_date(self, on_date):
        try:
            self.get_connection()
            self.cur.execute('''
                            SELECT f.id AS id, f.departure_date AS "departure_date", f.departure_time AS "departure_time", 
                             a1.name AS "departure_airport", l1.city AS "departure_city", l1.country AS "departure_country", 
                             a2.name AS "destination_airport", l2.city AS "destination_city", l2.country AS "destination_country", 
                             s.text AS "status" 
                            FROM flight f, airport a1, airport a2, status s, location l1, location l2
                            WHERE 
                             f.departure_airport_id=a1.id 
                             AND f.destination_airport_id=a2.id 
                             AND f.status_id=s.id 
                             AND a1.location_id=l1.id 
                             AND a2.location_id=l2.id
                             AND f.departure_date = ?
                             ORDER BY f.departure_time ASC
                             ''', (on_date,))
            rows = self.cur.fetchall()  # query results as list of sqlite3 Row objects
            results = [dict(row) for row in rows]   # transform query results as list of dictionaries with column names as keys
            return results

        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    ###############################################################################################################################
    def select_flights_by_departure_airport(self, airport_id):    #TODO: merge with below
        try:
            self.get_connection()
            self.cur.execute('''
                            SELECT f.id AS id, f.departure_date AS "departure_date", f.departure_time AS "departure_time", 
                             a1.name AS "departure_airport", l1.city AS "departure_city", l1.country AS "departure_country", 
                             a2.name AS "destination_airport", l2.city AS "destination_city", l2.country AS "destination_country", 
                             s.text AS "status" 
                            FROM flight f, airport a1, airport a2, status s, location l1, location l2
                            WHERE 
                             f.departure_airport_id=? 
                             AND f.departure_airport_id=a1.id                              
                             AND f.destination_airport_id=a2.id 
                             AND f.status_id=s.id 
                             AND a1.location_id=l1.id 
                             AND a2.location_id=l2.id
                             AND f.departure_date > date('now')
                             ORDER BY f.departure_date, f.departure_time ASC
                             ''', (airport_id,))
            rows = self.cur.fetchall()  # query results as list of sqlite3 Row objects
            results = [dict(row) for row in rows]   # transform query results as list of dictionaries with column names as keys
            return results

        except Exception as e:
            print(e)
        finally:
            self.conn.close()


    ###############################################################################################################################
    def select_all_past_flights(self):
        try:
            self.get_connection()
            self.cur.execute('''
                            SELECT f.id AS id, f.departure_date AS "departure_date", f.departure_time AS "departure_time", 
                             a1.name AS "departure_airport", l1.city AS "departure_city", l1.country AS "departure_country", 
                             a2.name AS "destination_airport", l2.city AS "destination_city", l2.country AS "destination_country", 
                             s.text AS "status" 
                            FROM flight f, airport a1, airport a2, status s, location l1, location l2
                            WHERE 
                             f.departure_airport_id=a1.id 
                             AND f.destination_airport_id=a2.id 
                             AND f.status_id=s.id 
                             AND a1.location_id=l1.id 
                             AND a2.location_id=l2.id
                             AND f.departure_date < date('now')
                             AND f.departure_time < time('now')
                             ORDER BY f.departure_date, f.departure_time DESC
                             ''')
            rows = self.cur.fetchall()  # query results as list of sqlite3 Row objects
            results = [dict(row) for row in rows]   # transform query results as list of dictionaries with column names as keys
            return results

        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    ###############################################################################################################################
    def update_flight(self, flight_id, field_to_update, field_new_value):

        try:
            self.get_connection()
            query = f"UPDATE flight SET {field_to_update} = ? WHERE id= ?"
            self.cur.execute(query, (field_new_value, flight_id,))
            self.conn.commit()
            return "successful update"

        except Exception as e:
            print(e)
            return "failed update"
        finally:
            self.conn.close()

    ###############################################################################################################################
    def delete_flight(self, flight_id):

        try:
            self.get_connection()
            query = f"DELETE FROM flight WHERE id= ?"
            self.cur.execute(query, (flight_id,))
            self.conn.commit()
            return "successful deletion"

        except Exception as e:
            print(e)
            return "failed deletion"
        finally:
            self.conn.close()



