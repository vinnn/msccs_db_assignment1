import sqlite3

from dbtables.pilotsTable import PilotsTable
from flight import FlightInfo
from airport import AirportInfo
from route import RouteInfo

# flights
# - date
# - time
# - status
# - route


# TODO: db.rollback





class DBOperations:
  
    sql_create_if_not_exist_table_schedule = "CREATE TABLE IF NOT EXISTS schedule ( \
        id INTEGER PRIMARY KEY AUTOINCREMENT, \
        flightNumber VARCHAR(10) NOT NULL REFERENCES flight(number), \
        statusId INTEGER NOT NULL REFERENCES status(id), \
        pilotId INTEGER NOT NULL REFERENCES pilot(id), \
        departureActualDate DATE NOT NULL, \
        departureActualTime TIME NOT NULL, \
        arrivalActualDate DATE NOT NULL, \
        arrivalActualTime TIME NOT NULL \
    );"

    sql_create_if_not_exist_table_flight = "CREATE TABLE IF NOT EXISTS flight ( \
        number VARCHAR(10) PRIMARY KEY, \
        originId INTEGER NOT NULL REFERENCES airport(id), \
        destinationId INTEGER NOT NULL REFERENCES airport(id), \
        departureTime TIME NOT NULL, \
        duration TIME NOT NULL \
    );"

    sql_create_if_not_exist_table_status = "CREATE TABLE IF NOT EXISTS status ( \
        id INTEGER PRIMARY KEY, \
        description VARCHAR(10) NOT NULL \
    );"

    # sql_create_if_not_exist_table_pilot = "CREATE TABLE IF NOT EXISTS pilot ( \
    #     id INTEGER PRIMARY KEY AUTOINCREMENT, \
    #     first_name VARCHAR(20) NOT NULL, \
    #     last_name VARCHAR(20) NOT NULL, \
    #     email VARCHAR(30) UNIQUE NOT NULL, \
    #     phone VARCHAR(16) UNIQUE NOT NULL \
    # );"

    sql_create_if_not_exist_table_airport = "CREATE TABLE IF NOT EXISTS airport ( \
        id INTEGER PRIMARY KEY AUTOINCREMENT, \
        name VARCHAR(20) NOT NULL, \
        city VARCHAR(20) NOT NULL, \
        country VARCHAR(20) NOT NULL \
    );"

    ############################################# 
    def __init__(self):
        try:
            self.conn = sqlite3.connect("airline.db")
            self.cur = self.conn.cursor()
            self.cur.execute(self.sql_create_if_not_exist_table_schedule)
            #   self.cur.execute('''SELECT * FROM pilot''')
            #   result = self.cur.fetchone()
            #   print(result)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    ############################################# 
    def get_connection(self):
        self.conn = sqlite3.connect("airline.db")
        self.cur = self.conn.cursor()
        

    ############################################# PILOTS      
    # def insert_new_pilot(self):
    #     try:
    #         self.get_connection()

    #         pilot = PilotInfo()
    #         pilot.set_first_name(input("Enter pilot first name: "))
    #         pilot.set_last_name(input("Enter pilot last name: "))
    #         pilot.set_email(input("Enter pilot email address: "))
    #         pilot.set_phone(input("Enter pilot phone number: "))

    #         sql_insert = "INSERT INTO pilot (first_name, last_name, email, phone) VALUES (?,?,?,?)"
    #         self.cur.execute(sql_insert, tuple(str(pilot).split("\n")))

    #         self.conn.commit()
    #         print("Inserted data successfully")
    #     except Exception as e:
    #         print(e)
    #     finally:
    #         self.conn.close()


    # def select_all_pilots(self):
    #     try:
    #         self.get_connection()
    #         self.cur.execute("SELECT * FROM pilot")
    #         results = self.cur.fetchall()

    #         headers = ["id","first name","last name", "email", "phone"]
    #         print("{:<6}{:<20}{:<20}{:<30}{:<16}".format(*headers)) # *: unpack argument sequence            
    #         # https://docs.python.org/2.7/library/string.html#format-specification-mini-language
    #         print("-" * 90)
    #         for row in results:
    #             print("{:<6}{:<20}{:<20}{:<30}{:<16}".format(*row))   # *: unpack argument sequence

    #     except Exception as e:
    #         print(e)
    #     finally:
    #         self.conn.close()


    ############################################# AIRPORTS      
    def insert_new_airport(self):
        try:
            self.get_connection()

            airport = AirportInfo()
            airport.set_name(input("Enter airport name: "))
            airport.set_city(input("Enter airport city name: "))
            airport.set_country(input("Enter airport country name: "))
            airport.set_weather(input("Enter airport local weather: "))

            sql_insert = "INSERT INTO airport (name, city, country, weather) VALUES (?,?,?,?)"
            self.cur.execute(sql_insert, tuple(str(airport).split("\n")))

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


    def select_all_airports(self):
        try:
            self.get_connection()
            self.cur.execute("SELECT * FROM airport")
            results = self.cur.fetchall()

            headers = ["id","name","city","country","weather"]
            print("{:<6}{:<50}{:<20}{:<20}{:<20}".format(*headers)) # *: unpack argument sequence            
            # https://docs.python.org/2.7/library/string.html#format-specification-mini-language
            print("-" * 106)
            for row in results:
                print("{:<6}{:<50}{:<20}{:<20}{:<20}".format(row[0], row[1][:48], row[2][:18], row[3][:18], row[4][:18]))   # *: unpack argument sequence
            print("-" * 106)

        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    ############################################# ROUTES      
    def insert_new_route(self):
        try:
            # show airport information (including ids) in order to create new route
            self.select_all_airports()

            route = RouteInfo()
            route.set_originId(input("Enter origin airport id: "))
            route.set_destinationId(input("Enter destination airport id: "))
            route.set_duration(input("Enter route flight duration (HR:MM:SS): "))

            self.get_connection()
            sql_insert = "INSERT INTO route (originId, destinationId, duration) VALUES (?,?,?)"
            self.cur.execute(sql_insert, tuple(str(route).split("\n")))

            self.conn.commit()
            print("Inserted data successfully")
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














    ############################################# 
    # def create_table(self):
    #     try:
    #         self.get_connection()
    #         self.cur.execute(self.sql_create_table)
    #         self.conn.commit()
    #         print("Table created successfully")
    #     except Exception as e:
    #         print(e)
    #     finally:
    #         self.conn.close()

    ############################################# 




    ############################################# 
    def search_data(self):
        try:
            self.get_connection()
            flightID = int(input("Enter FlightNo: "))
            self.cur.execute(self.sql_search, tuple(str(flightID)))
            result = self.cur.fetchone()
            if type(result) == type(tuple()):
                for index, detail in enumerate(result):
                    if index == 0:
                        print("Flight ID: " + str(detail))
                    elif index == 1:
                        print("Flight Origin: " + detail)
                    elif index == 2:
                        print("Flight Destination: " + detail)
                    else:
                        print("Status: " + str(detail))
            else:
                print("No Record")

        except Exception as e:
            print(e)
        finally:
            self.conn.close()



    ############################################# 
    def select_all(self):
        try:
            self.get_connection()
            self.cur.execute(self.sql_select_all)
            result = self.cur.fetchall()

            # think how you could develop this method to show the records

        except Exception as e:
            print(e)
        finally:
            self.conn.close()






    ############################################# 
    def update_data(self):
        try:
            self.get_connection()

            # Update statement

            if result.rowcount != 0:
                print(str(result.rowcount) + "Row(s) affected.")
            else:
                print("Cannot find this record in the database")

        except Exception as e:
            print(e)
        finally:
            self.conn.close()


    # Define Delete_data method to delete data from the table. The user will need to input the flight id to delete the corrosponding record.

    def delete_data(self):
        try:
            self.get_connection()

            if result.rowcount != 0:
                print(str(result.rowcount) + "Row(s) affected.")
            else:
                print("Cannot find this record in the database")

        except Exception as e:
            print(e)
        finally:
            self.conn.close()

