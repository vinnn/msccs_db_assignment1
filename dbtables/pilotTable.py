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


    def select_all_pilots(self):
        try:
            self.get_connection()
            # LEFT JOIN for location IN ORDER TO SHOW RESULTS EVEN IF NO LOCATION MATCHING
            self.cur.execute('''
                            SELECT p.id AS id, p.first_name AS "first_name", p.last_name AS "last_name", p.email AS "email", p.phone AS "phone", l.city AS "current_location_city", l.country AS "current_location_country"
                            FROM pilot p
                             LEFT JOIN location l ON p.current_location_id=l.id 
                            ''')
            rows = self.cur.fetchall()  # query results as list of sqlite3 Row objects
            results = [dict(row) for row in rows]   # transform query results as list of dictionaries with column names as keys
            return results

        except Exception as e:
            print(e)
        finally:
            self.conn.close()


    def select_all_pilots_available_by_period(self, from_datetime, to_datetime):

        query_clash_or_free = '''
                            SELECT f.id, f.pilot_id, f.departure_datetime AS "flight_from", f.arrival_datetime AS "flight_to",
                                CASE 
                                    WHEN (flight_from < from_datetime AND flight_to < from_datetime) OR (flight_from > to_datetime AND flight_to > to_datetime) 
                                    THEN "yes"
                                    ELSE "no"
                                END AS "available"
                            FROM flight f
                            '''

        query = '''
                WITH availability AS (
                    SELECT f.id AS flight_id, f.pilot_id AS pilot_id, f.departure_datetime AS "flight_from", f.arrival_datetime AS "flight_to",
                        CASE 
                            WHEN (flight_from < from_datetime AND flight_to < from_datetime) OR (flight_from > to_datetime AND flight_to > to_datetime) 
                            THEN "yes"
                            ELSE "no"
                        END AS "available"
                    FROM flight f
                )
                SELECT p.id, p.first_name, p.last_name
                FROM pilot p
                LEFT JOIN availability a ON p.id=a.pilot_id 
                WHERE a.available="yes"
                '''


            # self.cur.execute('''
            #     WITH availability AS (
            #         SELECT f.id, f.pilot_id, 
            #                  f.departure_datetime, 
            #                  strftime('%Y-%m-%d %H:%M', datetime(f.departure_datetime, '+' || f.duration)),
            #             CASE 
            #                 WHEN (f.departure_datetime < ? AND strftime('%Y-%m-%d %H:%M', datetime(f.departure_datetime, '+' || f.duration)) < ?) 
            #                  OR (f.departure_datetime > ? AND strftime('%Y-%m-%d %H:%M', datetime(f.departure_datetime, '+' || f.duration)) > ?) 
            #                 THEN "yes"
            #                 ELSE "no"
            #             END AS "available"
            #         FROM flight f
            #     )
            #     SELECT DISTINCT p.id, p.first_name, p.last_name, p.email, p.phone
            #     FROM pilot p
            #     LEFT JOIN availability a ON p.id=a.pilot_id
            #     WHERE a.available="yes"
            #     ORDER BY p.id ASC
            # ''', (from_datetime, from_datetime, to_datetime, to_datetime))


        try:
            self.get_connection()
            # LEFT JOIN for location IN ORDER TO SHOW RESULTS EVEN IF NO LOCATION MATCHING
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






    ############################################# 
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






