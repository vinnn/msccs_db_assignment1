
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # departure_airport_id INTEGER NOT NULL REFERENCES airport(id),
    # destination_airport_id INTEGER NOT NULL REFERENCES airport(id),
    # status_id INTEGER NOT NULL REFERENCES status(id),
    # pilot_id INTEGER NOT NULL REFERENCES pilot(id),
    # departure_date DATE NOT NULL,
    # departure_time TIME NOT NULL

# class Flight:

#     def __init__(self):
#         self.id = None
#         self.departure_airport_id = None        
#         self.destination_airport_id = None       
#         self.status_id = 0
#         self.pilot_id = None
#         self.departure_date = None
#         self.departure_time = None

#     def set_departure_airport_id(self, departure_airport_id):
#         self.departure_airport_id = departure_airport_id

#     def set_destination_airport_id(self, destination_airport_id):
#         self.destination_airport_id = destination_airport_id

#     def set_status_id(self, status_id):
#         self.status_id = status_id

#     def set_pilot_id(self, pilot_id):
#         self.pilot_id = pilot_id

#     def set_departure_date(self, departure_date):
#         self.departure_dateDate = departure_date

#     def set_departure_time(self, departure_time):
#         self.departure_time = departure_time

#     def set_duration(self, duration):
#         self.duration = duration

#     def set_destination_date(self, destination_date):
#         self.destination_date = destination_date

#     def set_destination_time(self, destination_time):
#         self.destination_time = destination_time

#     def __str__(self):     # this can then be called as :  str(pilot)
#         returnStr = self.departure_airport_id + "\n" + self.destination_airport_id + "\n" + str(self.statusId) + "\n" + str(self.pilotId) + "\n" + self.departureDate + "\n" + self.departureTime 
#         return returnStr

