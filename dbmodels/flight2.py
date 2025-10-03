
from utils import add_duration_to_datetime

    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # departure_airport_id INTEGER NOT NULL REFERENCES airport(id),
    # destination_airport_id INTEGER NOT NULL REFERENCES airport(id),
    # status_id INTEGER NOT NULL REFERENCES status(id),
    # pilot_id INTEGER NOT NULL REFERENCES pilot(id),
    # departure_date DATE NOT NULL,
    # departure_time TIME NOT NULL

class Flight2:

    def __init__(self, row):

        self.id = row.id if row.id else None
        
        self.status_id = row.status_id if row.status_id else None

        self.pilot_id = row.pilot_id if row.pilot_id else None
        self.pilot_first_name = row.pilot_first_name if row.pilot_first_name else None
        self.pilot_last_name = row.pilot_last_name if row.pilot_last_name else None

        self.departure_airport_id = row.departure_airport_id if row.departure_airport_id else None       
        self.arrival_airport_id = row.arrival_airport_id if row.arrival_airport_id else None  

        self.departure_datetime = row.departure_datetime if row.departure_datetime else None
        self.duration = row.duration if row.duration else None
        self.arrival_datetime = add_duration_to_datetime(row.departure_datetime, row.duration) if (row.departure_datetime is not None and row.duration is not None) else None



    def set_departure_airport_id(self, departure_airport_id):
        self.departure_airport_id = departure_airport_id

    def set_destination_airport_id(self, destination_airport_id):
        self.destination_airport_id = destination_airport_id

    def set_status_id(self, status_id):
        self.status_id = status_id

    def set_pilot_id(self, pilot_id):
        self.pilot_id = pilot_id

    def set_departure_date(self, departure_date):
        self.departure_dateDate = departure_date

    def set_departure_time(self, departure_time):
        self.departure_time = departure_time

    def set_duration(self, duration):
        self.duration = duration

    def set_destination_date(self, destination_date):
        self.destination_date = destination_date

    def set_destination_time(self, destination_time):
        self.destination_time = destination_time

    def set_new_flight(self, id, departure_airport_id, destination_airport_id, status_id, pilot_id, departure_date, departure_time, duration):
        self.set_departure_airport_id(departure_airport_id)
        self.set_destination_airport_id(destination_airport_id)
        self.set_status_id(status_id)
        self.set_pilot_id(pilot_id)
        self.set_departure_date(departure_date)
        self.set_departure_time(departure_time)
        self.set_duration(duration)
        




    def __str__(self):     # this can then be called as :  str(pilot)
        returnStr = self.departure_airport_id + "\n" + self.destination_airport_id + "\n" + str(self.statusId) + "\n" + str(self.pilotId) + "\n" + self.departureDate + "\n" + self.departureTime + "\n" + self.duration
        return returnStr

