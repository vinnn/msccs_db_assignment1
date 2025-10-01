import sqlite3
from dbmodels.route import Route
from dbtables.airportTable import AirportTable


class RouteTable:

    sql_create_if_not_exist_table = "CREATE TABLE IF NOT EXISTS route ( \
        id INTEGER PRIMARY KEY AUTOINCREMENT, \
        originId INTEGER NOT NULL REFERENCES airport(id), \
        destinationId INTEGER NOT NULL REFERENCES airport(id), \
        duration TIME NOT NULL \
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
    def insert_new_route(self):
        try:
            # show airport information (including ids) in order to create new route
            airportTable = AirportTable()
            airportTable.select_all_airports()

            route = Route()
            route.set_originId(input("Enter origin airport id: "))
            route.set_destinationId(input("Enter destination airport id: "))
            route.set_duration(input("Enter route flight duration (HR:MM:SS): "))

            self.get_connection()
            sql_insert = "INSERT INTO route (originId, destinationId, duration) VALUES (?,?,?)"
            self.cur.execute(sql_insert, tuple(str(route).split("\n")))

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


    def select_all_routes(self):
        try:
            self.get_connection()
            self.cur.execute("SELECT r.id, a1.name, a1.city, a1.country, a2.name, a2.city, a2.country, r.duration FROM route r, airport a1, airport a2 WHERE r.originId=a1.id AND r.destinationId=a2.id")
            results = self.cur.fetchall()

            headers = ["id","origin airport","city", "country", "destination airport", "city", "country", "duration"]
            print("{:<6}{:<20}{:<16}{:<16}{:<20}{:<16}{:<16}{:<12}".format(*headers)) # *: unpack argument sequence            
            print("-" * 120)
            for row in results:
                print("{:<6}{:<20}{:<16}{:<16}{:<20}{:<16}{:<16}{:<12}".format(row[0], row[1][:18], row[2][:14], row[3][:14], row[4][:18], row[5][:14], row[6][:14], row[7][:10]))   # *: unpack argument sequence
            print("-" * 120)

        except Exception as e:
            print(e)
        finally:
            self.conn.close()


