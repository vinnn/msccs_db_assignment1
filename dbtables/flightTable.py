import sqlite3
from dbtables.airportTable import AirportTable
from dbtables.pilotTable import PilotTable




class FlightTable:

    sql_create_if_not_exist_table = "CREATE TABLE IF NOT EXISTS flight ( \
        id INTEGER PRIMARY KEY AUTOINCREMENT, \
        routeId VARCHAR(10) NOT NULL REFERENCES route(id), \
        statusId INTEGER NOT NULL REFERENCES status(id), \
        pilotId INTEGER NOT NULL REFERENCES pilot(id), \
        departureDatetime DATETIME NOT NULL, \
        duration TIME NOT NULL \
    );"   #TODO: update

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
    def select_all_future_flights(self):
        try:
            self.get_connection()

            # formatting and create new columns
            # - LEFT JOIN the pilot table so that we have all rows of the flight table. And the column 'pilot' will contain 
            # the pilot ids in the pilot table, or None if not found (eg if a pilot has been deleted) 
            self.cur.execute('''
                            SELECT f.id AS id, 
                             date(f.departure_datetime) AS "departure_date", 
                             strftime('%H:%M', time(f.departure_datetime)) AS "departure_time",
                             strftime('%Y-%m-%d', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_date",
                             strftime('%H:%M', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_time",                             
                             a1.name AS "departure_airport", a1.city AS "departure_city", a1.country AS "departure_country", 
                             a2.name AS "arrival_airport", a2.city AS "arrival_city", a2.country AS "arrival_country", 
                             s.text AS "status",
                             p.id AS "pilot"
                            FROM flight f, airport a1, airport a2, status s
                             LEFT JOIN pilot p ON f.pilot_id = p.id
                            WHERE 
                             f.departure_airport_id=a1.id 
                             AND f.arrival_airport_id=a2.id 
                             AND f.status_id=s.id 
                             AND datetime(f.departure_datetime) > datetime('now', 'localtime')          
                             ORDER BY datetime(f.departure_datetime) ASC
                             ''')
            rows = self.cur.fetchall()  # query results as list of sqlite3 Row objects
            results = [dict(row) for row in rows]   # transform query results as list of dictionaries with column names as keys
            return results

        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    ###############################################################################################################################
    def select_all_future_unassigned_flights(self):
        try:
            self.get_connection()

            # formatting and create new columns
            self.cur.execute('''
                            SELECT f.id AS id,
                             date(f.departure_datetime) AS "departure_date",
                             strftime('%H:%M', time(f.departure_datetime)) AS "departure_time",
                             strftime('%Y-%m-%d', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_date",
                             strftime('%H:%M', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_time",              
                             a1.name AS "departure_airport", a1.city AS "departure_city", a1.country AS "departure_country",
                             a2.name AS "arrival_airport", a2.city AS "arrival_city", a2.country AS "arrival_country", 
                             s.text AS "status",
                             p.id AS "pilot"
                            FROM flight f, airport a1, airport a2, status s
                            LEFT JOIN pilot p ON p.id=f.pilot_id
                            WHERE
                             f.departure_airport_id=a1.id
                             AND f.arrival_airport_id=a2.id
                             AND f.status_id=s.id
                             AND (f.pilot_id IS NULL OR p.id IS NULL)
                             AND f.departure_datetime > datetime('now', 'localtime')
                             ORDER BY f.departure_datetime ASC
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
                            SELECT f.id AS id, 
                             date(f.departure_datetime) AS "departure_date", 
                             strftime('%H:%M', time(f.departure_datetime)) AS "departure_time",
                             strftime('%Y-%m-%d', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_date",
                             strftime('%H:%M', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_time",
                             f.duration AS "duration",
                             a1.name AS "departure_airport", a1.city AS "departure_city", a1.country AS "departure_country",
                             a2.name AS "arrival_airport", a2.city AS "arrival_city", a2.country AS "arrival_country",
                             s.text AS "status",
                             p.id AS "pilot_id", p.first_name AS "pilot_first_name", p.last_name AS "pilot_last_name"
                            FROM flight f, airport a1, airport a2, status s
                             LEFT JOIN pilot p ON f.pilot_id=p.id
                            WHERE
                             f.id=?
                             AND f.departure_airport_id=a1.id 
                             AND f.arrival_airport_id=a2.id 
                             AND f.status_id=s.id 
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
    def select_flights_by_departure_datetime(self, on_datetime):
        try:
            self.get_connection()
            self.cur.execute('''
                            SELECT DISTINCT f.id AS id, 
                             date(f.departure_datetime) AS "departure_date", 
                             strftime('%H:%M', time(f.departure_datetime)) AS "departure_time",
                             strftime('%Y-%m-%d', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_date",
                             strftime('%H:%M', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_time",                             
                             a1.name AS "departure_airport", a1.city AS "departure_city", a1.country AS "departure_country", 
                             a2.name AS "arrival_airport", a2.city AS "arrival_city", a2.country AS "arrival_country", 
                             s.text AS "status",
                             p.id AS "pilot"
                            FROM flight f, airport a1, airport a2, status s
                             LEFT JOIN pilot p ON f.pilot_id = p.id                             
                            WHERE 
                             f.departure_airport_id=a1.id 
                             AND f.arrival_airport_id=a2.id 
                             AND f.status_id=s.id 
                             AND strftime('%Y-%m-%d', f.departure_datetime) = strftime('%Y-%m-%d', ?)
                             ORDER BY f.departure_datetime ASC
                             ''', (on_datetime,))
            rows = self.cur.fetchall()  # query results as list of sqlite3 Row objects
            results = [dict(row) for row in rows]   # transform query results as list of dictionaries with column names as keys
            return results

        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    ###############################################################################################################################
    def select_flights_by_departure_airport(self, airport_id):
        try:
            self.get_connection()
            self.cur.execute('''
                            SELECT DISTINCT f.id AS id, 
                             date(f.departure_datetime) AS "departure_date", 
                             strftime('%H:%M', time(f.departure_datetime)) AS "departure_time",
                             strftime('%Y-%m-%d', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_date",
                             strftime('%H:%M', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_time",                             
                             a1.name AS "departure_airport", a1.city AS "departure_city", a1.country AS "departure_country", 
                             a2.name AS "arrival_airport", a2.city AS "arrival_city", a2.country AS "arrival_country", 
                             s.text AS "status",
                             p.id AS "pilot"
                            FROM flight f, airport a1, airport a2, status s
                             LEFT JOIN pilot p ON f.pilot_id = p.id                             
                            WHERE 
                             f.departure_airport_id=? 
                             AND f.departure_airport_id=a1.id                              
                             AND f.arrival_airport_id=a2.id 
                             AND f.status_id=s.id 
                             AND f.departure_datetime > datetime('now', 'localtime')
                             ORDER BY f.departure_datetime ASC
                             ''', (airport_id,))
            rows = self.cur.fetchall()  # query results as list of sqlite3 Row objects
            results = [dict(row) for row in rows]   # transform query results as list of dictionaries with column names as keys
            return results

        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    ###############################################################################################################################
    def select_flights_by_arrival_airport(self, airport_id):
        try:
            self.get_connection()
            self.cur.execute('''
                            SELECT DISTINCT f.id AS id, 
                             date(f.departure_datetime) AS "departure_date", 
                             strftime('%H:%M', time(f.departure_datetime)) AS "departure_time",
                             strftime('%Y-%m-%d', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_date",
                             strftime('%H:%M', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_time",                             
                             a1.name AS "departure_airport", a1.city AS "departure_city", a1.country AS "departure_country", 
                             a2.name AS "arrival_airport", a2.city AS "arrival_city", a2.country AS "arrival_country", 
                             s.text AS "status",
                             p.id AS "pilot"
                            FROM flight f, airport a1, airport a2, status s
                             LEFT JOIN pilot p ON f.pilot_id = p.id                             
                            WHERE 
                             f.arrival_airport_id=? 
                             AND f.departure_airport_id=a1.id                              
                             AND f.arrival_airport_id=a2.id 
                             AND f.status_id=s.id 
                             AND f.departure_datetime > datetime('now', 'localtime')
                             ORDER BY f.departure_datetime ASC
                             ''', (airport_id,))
            rows = self.cur.fetchall()  # query results as list of sqlite3 Row objects
            results = [dict(row) for row in rows]   # transform query results as list of dictionaries with column names as keys
            return results

        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    ###############################################################################################################################
    def select_flights_by_pilot(self, pilot_id):
        try:
            self.get_connection()
            self.cur.execute('''
                            SELECT DISTINCT f.id AS id, 
                             date(f.departure_datetime) AS "departure_date", 
                             strftime('%H:%M', time(f.departure_datetime)) AS "departure_time",
                             strftime('%Y-%m-%d', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_date",
                             strftime('%H:%M', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_time",                             
                             a1.name AS "departure_airport", a1.city AS "departure_city", a1.country AS "departure_country", 
                             a2.name AS "arrival_airport", a2.city AS "arrival_city", a2.country AS "arrival_country", 
                             s.text AS "status",
                             p.id AS "pilot"
                            FROM flight f, airport a1, airport a2, status s
                             LEFT JOIN pilot p ON f.pilot_id = p.id
                            WHERE 
                             f.pilot_id=? 
                             AND f.departure_airport_id=a1.id
                             AND f.arrival_airport_id=a2.id 
                             AND f.status_id=s.id 
                             AND datetime(f.departure_datetime) > datetime('now', 'localtime')
                             ORDER BY f.departure_datetime ASC
                             ''', (pilot_id,))
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
                            SELECT f.id AS id, 
                             date(f.departure_datetime) AS "departure_date", 
                             strftime('%H:%M', time(f.departure_datetime)) AS "departure_time",
                             strftime('%Y-%m-%d', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_date",
                             strftime('%H:%M', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_time",                             
                             a1.name AS "departure_airport", a1.city AS "departure_city", a1.country AS "departure_country", 
                             a2.name AS "arrival_airport", a2.city AS "arrival_city", a2.country AS "arrival_country", 
                             s.text AS "status",
                             p.id AS "pilot"
                            FROM flight f, airport a1, airport a2, status s
                             LEFT JOIN pilot p ON f.pilot_id = p.id                             
                            WHERE 
                             f.departure_airport_id=a1.id 
                             AND f.arrival_airport_id=a2.id 
                             AND f.status_id=s.id 
                             AND f.departure_datetime < datetime('now', 'localtime')                          
                             ORDER BY f.departure_datetime DESC
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

    ###############################################################################################################################
    def create_flight(self, data):
        try:
            self.get_connection()
            query = f"INSERT INTO flight (departure_airport_id, arrival_airport_id, status_id, pilot_id, departure_datetime, duration) VALUES (?,?,?,?,?,?)"
            self.cur.execute(query, 
                             (int(data["departure_airport_id"]), 
                              int(data["arrival_airport_id"]), 
                              int(data["status_id"]), 
                              int(data["pilot_id"]), 
                              data["departure_datetime"].strftime("%Y-%m-%d %H:%M") , 
                              data["duration"], 
                              )
                            )
            self.conn.commit()
            return "successful creation"

        except Exception as e:
            print(e)
            return "failed creation"
        finally:
            self.conn.close()

    ###############################################################################################################################
    def select_nb_status_ytd_pc(self, status_id):
        try:
            self.get_connection()
            self.cur.execute(f"""
                    SELECT 
                    CASE 
                        WHEN (
                            SELECT COUNT(*) FROM flight f 
                                WHERE datetime(f.departure_datetime) >= datetime(strftime('%Y-01-01', 'now'))
                                AND datetime(f.departure_datetime) < datetime('now')
                            ) = 0 
                        THEN NULL
                        ELSE (
                            SELECT COUNT(*) FROM flight f 
                                WHERE f.status_id={status_id}
                                AND datetime(f.departure_datetime) >= datetime(strftime('%Y-01-01', 'now'))
                                AND datetime(f.departure_datetime) < datetime('now')
                            ) * 1.0 
                            / (
                            SELECT COUNT(*) FROM flight f 
                                WHERE datetime(f.departure_datetime) >= datetime(strftime('%Y-01-01', 'now'))
                                AND datetime(f.departure_datetime) < datetime('now')
                            )
                        END AS result_pc;            
            """)

            row = self.cur.fetchone()  # query results as list of sqlite3 Row objects
            result = dict(row)
            return result["result_pc"]

        except Exception as e:
            print(e)
            return "failed select"
        finally:
            self.conn.close()

    ###############################################################################################################################
    def select_nb_unassigned_scheduled_flights(self):
        try:
            self.get_connection()
            self.cur.execute(f"""
                    SELECT COUNT(f.id) AS result_nb
                    FROM flight f, airport a1, airport a2, status s
                    LEFT JOIN pilot p ON p.id=f.pilot_id
                    WHERE
                        f.departure_airport_id=a1.id
                        AND f.arrival_airport_id=a2.id
                        AND f.status_id=s.id
                        AND (f.pilot_id IS NULL OR p.id IS NULL)
                        AND datetime(f.departure_datetime) > datetime('now', 'localtime')
                        ORDER BY f.departure_datetime ASC;          
            """)
            
            row = self.cur.fetchone()  # query results as list of sqlite3 Row objects
            result = dict(row)
            return result["result_nb"]

        except Exception as e:
            print(e)
            return "failed select"
        finally:
            self.conn.close()


