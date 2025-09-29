



 CREATE TABLE flight (
    number VARCHAR(10) NOT NULL,
    originId INTEGER NOT NULL,
    destinationId INTEGER NOT NULL,
    departureTime DATE NOT NULL,
    PRIMARY KEY (number),
    FOREIGN KEY (originId) REFERENCES location(id),
    FOREIGN KEY (destinationId) REFERENCES location(id)
)


 CREATE TABLE schedule (
    id INTEGER UNSIGNED NOT NULL AUTOINCREMENT,
    flightNumber VARCHAR(10) NOT NULL,
    statusId INTEGER NOT NULL,
    departureActualDate DATE NOT NULL,
    departureActualTime TIME NOT NULL,
    arrivalActualDate DATE NOT NULL,
    arrivalActualTime TIME NOT NULL,
    pilotId INTEGER NOT NULL
    PRIMARY KEY (id),
    FOREIGN KEY (flightNumber) REFERENCES flight(number),    
    FOREIGN KEY (statusId) REFERENCES status(id),
    FOREIGN KEY (pilotId) REFERENCES pilot(id)    
)

 CREATE TABLE status (
    id INTEGER NOT NULL,
    description VARCHAR(10) NOT NULL,
    PRIMARY KEY (id)    
)

 CREATE TABLE pilot (
    id INTEGER NOT NULL,
    name VARCHAR(20) NOT NULL,
    email VARCHAR(30),
    phone VARCHAR(16),
    PRIMARY KEY (id)
)

 CREATE TABLE location (
    id INTEGER NOT NULL,
    name VARCHAR(20) NOT NULL,
    PRIMARY KEY (id)
)

