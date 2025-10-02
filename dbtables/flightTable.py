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


    ############################################# 
    def insert_new_flight(self):
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
                             AND f.departure_date > date('now')
                             ''')
            rows = self.cur.fetchall()  # query results as list of sqlite3 Row objects
            results = [dict(row) for row in rows]   # transform query results as list of dictionaries with column names as keys
            return results

        except Exception as e:
            print(e)
        finally:
            self.conn.close()


    # def select_all_flights(self):
    #     try:
    #         self.get_connection()
    #         self.cur.execute('''
    #                         SELECT f.id, f.departure_date, f.departure_time, a1.name, l1.city, l1.country, a2.name, l2.city, l2.country, s.text 
    #                         FROM flight f, airport a1, airport a2, status s, location l1, location l2
    #                         WHERE f.departure_airport_id=a1.id AND f.destination_airport_id=a2.id AND f.status_id=s.id AND a1.location_id=l1.id AND a2.location_id=l2.id
    #                          ''')
    #         results = self.cur.fetchall()

    #         # print(results)

    #         headers = ["id","departure date", "time","from airport","city", "country","to airport","city","country","status"]
    #         formatsize = "{:<6}{:<18}{:<14}{:<20}{:<16}{:<16}{:<20}{:<16}{:<16}{:<12}"
    #         print(formatsize.format(*headers)) # *: unpack argument sequence            
    #         print("-" * 150)
    #         for row in results:
    #             print(formatsize.format(row[0], row[1][:10], row[2][:10], row[3][:16], row[4][:12], row[5][:12], row[6][:16], row[7][:12], row[8][:12], row[9]))   # *: unpack argument sequence
    #         print("-" * 150)

    #     except Exception as e:
    #         print(e)
    #     finally:
    #         self.conn.close()




    def select_one_flight(self, flight_id):
        try:
            self.get_connection()
            self.cur.execute('''
                            SELECT f.id AS id, f.departure_date AS "departure_date", f.departure_time AS "departure_time", 
                             a1.name AS "departure_airport", l1.city AS "departure_city", l1.country AS "departure_country", 
                             a2.name AS "destination_airport", l2.city AS "destination_city", l2.country AS "destination_country", 
                             s.text AS "status", 
                             p.first_name AS "pilot_first_name", p.last_name AS "pilot_last_name" 
                            FROM flight f, airport a1, airport a2, status s, location l1, location l2, pilot p
                            WHERE 
                             f.departure_airport_id=a1.id 
                             AND f.destination_airport_id=a2.id 
                             AND f.status_id=s.id 
                             AND a1.location_id=l1.id 
                             AND a2.location_id=l2.id
                             AND f.pilot_id=p.id
                             AND f.id=?
                             ''',
                             (flight_id,)
                             )
            
            row = self.cur.fetchone()  # query result as sqlite3 Row object
            print(row)

            result = dict(row) if row is not None else None  # transform query result as dictionary with column names as keys

            print(result)

            return result

        except Exception as e:
            print(e)
        finally:
            self.conn.close()








    # def select_one_flight(self, flightId):
    #     try:
    #         self.get_connection()       
    #         sql_select = '''
    #                         SELECT f.id, f.departureDate, f.departureTime, a1.name, a1.city, a1.country, a2.name, a2.city, a2.country, r.duration, s.text, p.first_name, p.last_name 
    #                         FROM flight f, route r, airport a1, airport a2, status s, pilot p
    #                         WHERE f.routeId = r.id AND r.originId=a1.id AND r.destinationId=a2.id AND f.statusId=s.id AND f.pilotId=p.id AND f.id=?
    #                          '''
    #         self.cur.execute(sql_select, (flightId,))

    #         result = self.cur.fetchone()

    #         print("-" * 80)            
    #         print("{:<24}{:<24}".format("flight id",result[0]))
    #         print("{:<24}{:<24}".format("departure date", result[1]))
    #         print("{:<24}{:<24}".format("departure time", result[2]))            
    #         print("{:<24}{:<24}".format("departure airport", result[3] + ", " + result[4] + ", " + result[5]))            
    #         print("{:<24}{:<24}".format("arrival airport", result[6] + ", " + result[7] + ", " + result[8]))
    #         print("{:<24}{:<24}".format("status", result[10]))
    #         print("{:<24}{:<24}".format("pilot", result[11] + " " + result[12]))  
    #         print("-" * 80)

    #     except Exception as e:
    #         print(e)
    #     finally:
    #         self.conn.close()