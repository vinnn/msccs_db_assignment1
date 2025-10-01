import sqlite3
from dbmodels.pilot import Pilot

class PilotsTable:

    sql_create_if_not_exist_table = "CREATE TABLE IF NOT EXISTS pilot ( \
        id INTEGER PRIMARY KEY AUTOINCREMENT, \
        first_name VARCHAR(20) NOT NULL, \
        last_name VARCHAR(20) NOT NULL, \
        email VARCHAR(30) UNIQUE NOT NULL, \
        phone VARCHAR(16) UNIQUE NOT NULL \
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
    def insert_new_pilot(self):
        try:
            self.get_connection()

            pilot = Pilot()
            pilot.set_first_name(input("Enter pilot first name: "))
            pilot.set_last_name(input("Enter pilot last name: "))
            pilot.set_email(input("Enter pilot email address: "))
            pilot.set_phone(input("Enter pilot phone number: "))

            sql_insert = "INSERT INTO pilot (first_name, last_name, email, phone) VALUES (?,?,?,?)"
            self.cur.execute(sql_insert, tuple(str(pilot).split("\n")))

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


    def select_all_pilots(self):
        try:
            self.get_connection()
            self.cur.execute("SELECT * FROM pilot")
            results = self.cur.fetchall()

            headers = ["id","first name","last name", "email", "phone"]
            print("{:<6}{:<20}{:<20}{:<30}{:<16}".format(*headers)) # *: unpack argument sequence            
            # https://docs.python.org/2.7/library/string.html#format-specification-mini-language
            print("-" * 90)
            for row in results:
                print("{:<6}{:<20}{:<20}{:<30}{:<16}".format(*row))   # *: unpack argument sequence

        except Exception as e:
            print(e)
        finally:
            self.conn.close()



