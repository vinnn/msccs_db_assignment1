


    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # ref VARCHAR(10),
    # originId INTEGER NOT NULL REFERENCES airport(id),
    # destinationId INTEGER NOT NULL REFERENCES airport(id),
    # duration TIME NOT NULL


class RouteInfo:

    def __init__(self):
        self.id = None
        self.originId = None
        self.destinationId = None
        self.duration = None

    def set_originId(self, originId):
        self.originId = originId

    def set_destinationId(self, destinationId):
        self.destinationId = destinationId

    def set_duration(self, duration):
        self.duration = duration

    def __str__(self):     # this can then be called as :  str(airport)
        returnStr = self.originId + "\n" + self.destinationId + "\n" + self.duration 
        return returnStr
