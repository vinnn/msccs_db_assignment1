import sqlite3
from dbmodels.pilot import Pilot

class PilotTable:

    sql_create_if_not_exist_table = "CREATE TABLE IF NOT EXISTS pilot ( \
        id INTEGER PRIMARY KEY AUTOINCREMENT, \
        first_name VARCHAR(20) NOT NULL, \
        last_name VARCHAR(20) NOT NULL, \
        email VARCHAR(30) UNIQUE NOT NULL, \
        phone VARCHAR(16) UNIQUE NOT NULL \
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
    def select_all_pilots(self):
        try:
            self.get_connection()
            # LEFT JOIN for location IN ORDER TO SHOW RESULTS EVEN IF NO LOCATION MATCHING
            self.cur.execute('''
                            SELECT p.id AS id, p.first_name AS "first_name", p.last_name AS "last_name", p.email AS "email", p.phone AS "phone"
                            FROM pilot p
                            ORDER BY id ASC
                            ''')
            rows = self.cur.fetchall()  # query results as list of sqlite3 Row objects
            results = [dict(row) for row in rows]   # transform query results as list of dictionaries with column names as keys
            return results

        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    ###############################################################################################################################
    def select_all_pilots_available_by_period(self, from_datetime, to_datetime):

        try:
            self.get_connection()
            # create a table of all flights that show if clash with the period
            # then select only the pilots of flights that have no clash 
            self.cur.execute('''     
                SELECT p.id, p.first_name, p.last_name, p.email, p.phone
                FROM pilot p
                WHERE p.id NOT IN (
                    SELECT pilot_id FROM 
                    (
                        SELECT f.pilot_id AS "pilot_id",
                            CASE 
                                WHEN strftime('%Y-%m-%d %H:%M', datetime(f.departure_datetime, '+' || f.duration)) < ?
                                    OR f.departure_datetime > ?
                                THEN 0
                                ELSE 1
                            END AS "clash"
                        FROM flight f
                        GROUP BY f.pilot_id
                        HAVING SUM(clash)>0
                    )
                )
            ''', (from_datetime, to_datetime))
            rows = self.cur.fetchall()  # query results as list of sqlite3 Row objects
            results = [dict(row) for row in rows]   # transform query results as list of dictionaries with column names as keys
            # print(results)
            return results

        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    ###############################################################################################################################
    def select_one_pilot(self, pilot_id):
        try:
            self.get_connection()
            self.cur.execute('''
                            SELECT id, first_name, last_name, email, phone
                            FROM pilot
                            WHERE id=?
                             ''',
                             (pilot_id,)
                             )
            
            row = self.cur.fetchone()  # query result as sqlite3 Row object
            result = dict(row) if row is not None else None  # transform query result as dictionary with column names as keys
            return result

        except Exception as e:
            print(e)
        finally:
            self.conn.close()


    ###############################################################################################################################
    def update_pilot(self, id, field_to_update, field_new_value):

        try:
            self.get_connection()
            query = f"UPDATE pilot SET {field_to_update} = ? WHERE id= ?"
            self.cur.execute(query, (field_new_value, id,))
            self.conn.commit()
            return "successful update"

        except Exception as e:
            print(e)
            return "failed update"
        finally:
            self.conn.close()


    ###############################################################################################################################
    def delete_pilot(self, id):

        try:
            self.get_connection()
            query = f"DELETE FROM pilot WHERE id= ?"
            self.cur.execute(query, (id,))
            self.conn.commit()
            return "successful deletion"

        except Exception as e:
            print(e)
            return "failed deletion"
        finally:
            self.conn.close()



    ###############################################################################################################################
    # def insert_new_pilot(self):
    #     try:
    #         self.get_connection()

    #         pilot = Pilot()
    #         pilot.set_first_name(input("Enter pilot first name: "))
    #         pilot.set_last_name(input("Enter pilot last name: "))
    #         pilot.set_email(input("Enter pilot email address: "))
    #         pilot.set_phone(input("Enter pilot phone number: "))

    #         sql_insert = "INSERT INTO pilot (first_name, last_name, email, phone) VALUES (?,?,?,?)"
    #         self.cur.execute(sql_insert, tuple(str(pilot).split("\n")))

    #         confirm = True if input("confirm creation (Y/N): ") == "Y" else False
    #         if confirm:
    #             self.conn.commit()
    #             print("Inserted data successfully")
    #         else:
    #             print("Cancelled insertion")

    #     except Exception as e:
    #         print(e)
    #     finally:
    #         self.conn.close()






