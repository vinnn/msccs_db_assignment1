import sqlite3
from dbmodels.flight import Flight
from dbtables.routeTable import RouteTable
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
        self.cur = self.conn.cursor()


    ############################################# 
    def insert_new_flight(self):
        try:
            flight = Flight()

            # show route information (including ids) in order to create new flight
            routeTable = RouteTable()
            routeTable.select_all_routes()

            flight.set_routeId(input("Enter route id: "))

            flight.set_departureDate(input("Enter flight detaprture date (YR-MM-DD): "))
            flight.set_departureTime(input("Enter flight detaprture time (HR:MM:SS): "))

            # show pilot information (including ids) in order to create new flight
            pliotTable = PilotTable()
            pliotTable.select_all_pilots()

            flight.set_pilotId(input("Enter flight pilot id: "))

            self.get_connection()
            sql_insert = "INSERT INTO flight (routeId, statusId, pilotId, departureDate, departureTime) VALUES (?,?,?,?,?)"
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


    def select_all_flights(self):
        try:
            self.get_connection()
            self.cur.execute('''
                            SELECT f.id, f.departureDate, f.departureTime, a1.name, a1.city, a1.country, a2.name, a2.city, a2.country, s.text 
                            FROM flight f, route r, airport a1, airport a2, status s
                            WHERE f.routeId = r.id AND r.originId=a1.id AND r.destinationId=a2.id AND f.statusId=s.id
                             ''')
            results = self.cur.fetchall()

            print(results)

            headers = ["id","departure date", "time","from airport","city", "country","to airport","city","country","status"]
            formatsize = "{:<6}{:<18}{:<14}{:<20}{:<16}{:<16}{:<20}{:<16}{:<16}{:<12}"
            print(formatsize.format(*headers)) # *: unpack argument sequence            
            print("-" * 150)
            for row in results:
                print(formatsize.format(row[0], row[1][:10], row[2][:10], row[3][:16], row[4][:12], row[5][:12], row[6][:16], row[7][:12], row[8][:12], row[9]))   # *: unpack argument sequence
            print("-" * 150)

        except Exception as e:
            print(e)
        finally:
            self.conn.close()


