
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # first_name VARCHAR(20) NOT NULL,
    # last_name VARCHAR(20) NOT NULL,
    # email VARCHAR(30) UNIQUE NOT NULL,
    # phone VARCHAR(16) UNIQUE NOT NULL


class PilotInfo:

    def __init__(self):
        self.id = None
        self.first_name = ''
        self.last_name = ''
        self.email = ''
        self.phone = ''

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_email(self, email):
        self.email = email

    def set_phone(self, phone):
        self.phone = phone        

    def __str__(self):     # this can then be called as :  str(pilot)
        returnStr = self.first_name + "\n" + self.last_name + "\n" + self.email + "\n" + self.phone 
        return returnStr
    

