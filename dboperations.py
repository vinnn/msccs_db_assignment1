import sqlite3

from pilot import PilotInfo

# flights
# - date
# - time
# - status
# - route


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

    sql_create_if_not_exist_table_pilot = "CREATE TABLE IF NOT EXISTS pilot ( \
        id INTEGER PRIMARY KEY AUTOINCREMENT, \
        first_name VARCHAR(20) NOT NULL, \
        last_name VARCHAR(20) NOT NULL, \
        email VARCHAR(30) UNIQUE NOT NULL, \
        phone VARCHAR(16) UNIQUE NOT NULL \
    );"

    sql_create_if_not_exist_table_airport = "CREATE TABLE IF NOT EXISTS airport ( \
        id INTEGER PRIMARY KEY AUTOINCREMENT, \
        name VARCHAR(20) NOT NULL, \
        city VARCHAR(20) NOT NULL, \
        country VARCHAR(20) NOT NULL \
    );"

 




#   sql_create_tables_firsttime = "" \
#   "CREATE TABLE IF NOT EXISTS schedule;" \
#     "CREATE TABLE IF NOT EXISTS flight;" \
#       "CREATE TABLE IF NOT EXISTS status;" \
#         "CREATE TABLE IF NOT EXISTS pilot;" \
#           "CREATE TABLE IF NOT EXISTS airport;"

#   sql_create_table = "CREATE TABLE TableName"

#   sql_insert = ""
#   sql_select_all = "SELECT * FROM pilot"
#   sql_search = "select * from TableName where FlightID = ?"
#   sql_alter_data = ""
#   sql_update_data = ""
#   sql_delete_data = ""
#   sql_drop_table = ""

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
        


    def insert_new_pilot(self):
        try:
            self.get_connection()

            pilot = PilotInfo()
            pilot.set_first_name(input("Enter pilot first name: "))
            pilot.set_last_name(input("Enter pilot last name: "))
            pilot.set_email(input("Enter pilot email address: "))
            pilot.set_phone(input("Enter pilot phone number: "))

            sql_insert = "INSERT INTO pilot (first_name, last_name, email, phone) VALUES (?,?,?,?)"
            self.cur.execute(sql_insert, tuple(str(pilot).split("\n")))

            self.conn.commit()
            print("Inserted data successfully")
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

