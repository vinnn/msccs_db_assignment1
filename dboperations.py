import sqlite3


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



    ############################################# 
    def __init__(self):
        try:
            self.conn = sqlite3.connect("airline.db")
            self.cur = self.conn.cursor()
            self.cur.execute(self.sql_create_if_not_exist_table_schedule)
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

