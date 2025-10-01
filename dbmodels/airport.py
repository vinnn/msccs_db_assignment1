
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name VARCHAR(20) NOT NULL,
    # city VARCHAR(20) NOT NULL,
    # country VARCHAR(20) NOT NULL


class Airport:

    def __init__(self):
        self.id = None
        self.name = None
        self.city = None
        self.country = None
        self.weather = None

    def set_name(self, name):
        self.name = name

    def set_city(self, city):
        self.city = city

    def set_country(self, country):
        self.country = country

    def set_weather(self, weather):
        self.weather = weather

    def __str__(self):     # this can then be called as :  str(airport)
        returnStr = self.name + "\n" + self.city + "\n" + self.country + "\n" + self.weather 
        return returnStr
