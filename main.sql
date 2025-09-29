

DROP TABLE flight;


 CREATE TABLE flight (
    number VARCHAR(10) PRIMARY KEY,
    originId INTEGER NOT NULL REFERENCES location(id),
    destinationId INTEGER NOT NULL REFERENCES location(id),
    departureTime DATE NOT NULL
);


 CREATE TABLE schedule (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    flightNumber VARCHAR(10) NOT NULL REFERENCES flight(number),
    statusId INTEGER NOT NULL REFERENCES status(id),
    pilotId INTEGER NOT NULL REFERENCES pilot(id),
    departureActualDate DATE NOT NULL,
    departureActualTime TIME NOT NULL,
    arrivalActualDate DATE NOT NULL,
    arrivalActualTime TIME NOT NULL
);

 CREATE TABLE status (
    id INTEGER PRIMARY KEY,
    description VARCHAR(10) NOT NULL 
);

 CREATE TABLE pilot (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(20) NOT NULL,
    email VARCHAR(30),
    phone VARCHAR(16)
);

 CREATE TABLE location (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(20) NOT NULL
);

