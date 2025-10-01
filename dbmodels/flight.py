
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # routeId VARCHAR(10) NOT NULL REFERENCES route(id),
    # statusId INTEGER NOT NULL REFERENCES status(id),
    # pilotId INTEGER NOT NULL REFERENCES pilot(id),
    # departureDate DATE NOT NULL,
    # departureTime TIME NOT NULL

class Flight:

    def __init__(self):
        self.id = None
        self.routeId = None
        self.statusId = 0
        self.pilotId = None
        self.departureDate = None
        self.departureTime = None

        # self.originId = None
        # self.destinationId = None  
        # self.origin = None
        # self.destinationId = None        
        # self.destination = None
        # self.departureDate = None
        # self.departureTime = None
        # self.arrivalDate = None
        # self.arrivalTime = None
        # self.status = None
        # self.pilotId = None
        # self.pilotFirstName = None
        # self.pilotLastName = None

    def set_routeId(self, routeId):
        self.routeId = routeId

    def set_statusId(self, statusId):
        self.statusId = statusId

    def set_pilotId(self, pilotId):
        self.pilotId = pilotId

    def set_departureDate(self, departureDate):
        self.departureDate = departureDate

    def set_departureTime(self, departureTime):
        self.departureTime = departureTime

    def __str__(self):     # this can then be called as :  str(pilot)
        returnStr = self.routeId + "\n" + str(self.statusId) + "\n" + str(self.pilotId) + "\n" + self.departureDate + "\n" + self.departureTime 
        return returnStr

