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
        self.cur = self.conn.cursor()

    ############################################# 
    def insert_new_airport(self):
        try:
            self.get_connection()

            airport = Airport()
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




