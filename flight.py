


class Flight:

    def __init__(self):
        self.id = None
        self.routeId = None
        self.routeRef = None
        self.origin = None
        self.destination = None
        self.departureDate = None
        self.departureTime = None
        self.arrivalDate = None
        self.arrivalTime = None
        self.status = None
        self.pilotId = None
        self.pilotFirstName = None
        self.pilotLastName = None

    def set_flight_routeId(self, routeId):
        self.routeId = routeId

    def set_flight_routeId(self, routeId):
        self.routeId = routeId



# class FlightInfo:

#   def __init__(self):
#     self.flightID = 0
#     self.flightOrigin = ''
#     self.flightDestination = ''
#     self.status = ''

#   def set_flight_id(self, flightID):
#     self.flightID = flightID

#   def set_flight_origin(self, flightOrigin):
#     self.flight_origin = flightOrigin

#   def set_flight_destination(self, flightDestination):
#     self.flight_destination = flightDestination

#   def set_status(self, status):
#     self.status = status

#   def get_flight_id(self):
#     return self.flightID

#   def get_flight_origin(self):
#     return self.flightOrigin

#   def get_flight_destination(self):
#     return self.flightDestination

#   def get_status(self):
#     return self.status

#   def __str__(self):
#     return str(
#       self.flightID
#     ) + "\n" + self.flightOrigin + "\n" + self.flightDestination + "\n" + str(
#       self.status)

