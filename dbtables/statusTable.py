import sqlite3

class StatusTable:

    sql_create_if_not_exist_table = """
        CREATE TABLE IF NOT EXISTS status (
            id INTEGER PRIMARY KEY,
            text VARCHAR(10) NOT NULL 
        );
    """

    ###############################################################################################################################
    def __init__(self):
        try:
            self.conn = sqlite3.connect("airline.db")
            self.conn.execute("PRAGMA foreign_keys = ON") # needed to enable foreign key support (eg enforce DELETE RESTRICT) https://sqlite.org/foreignkeys.html            
            self.cur = self.conn.cursor()
            self.cur.execute(self.sql_create_if_not_exist_table)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.conn.close()
