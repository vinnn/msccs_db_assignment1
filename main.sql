

-- check the table just created:
. schema
-- check the list of tables:
. table



DROP TABLE IF EXISTS flight;
DROP TABLE IF EXISTS schedule;
DROP TABLE IF EXISTS status;
DROP TABLE IF EXISTS pilot;
DROP TABLE IF EXISTS airport;


 CREATE TABLE flight (
    number VARCHAR(10) PRIMARY KEY,
    originId INTEGER NOT NULL REFERENCES airport(id),
    destinationId INTEGER NOT NULL REFERENCES airport(id),
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
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    email VARCHAR(30) UNIQUE NOT NULL,
    phone VARCHAR(16) UNIQUE NOT NULL
);



INSERT INTO pilot (first_name, last_name, email, phone) VALUES
('Steve', 'Lewis', 's.lewis@yesairways', '0849384738202'),
('Josh', 'Tambo', 'j.tambo@yesairways', '0849389873642'),
('Sylvie', 'Aritin', 's.aritin@yesairways', '0839876462737'),
('Joseph', 'Dimst', 'j.dimst@yesairways', '0898346493877'),
('Aruna', 'Reno', 'a.reno@yesairways', '0837648376438'),
('Bill', 'Farr', 'b.farr@yesairways', '0852374203846'),
('Max', 'Himtas', 'm.himtas@yesairways', '0899846288872'),
('Bob', 'Hewitt', 'b.hewitt@yesairways', '0852837698379'),
('Marina', 'Bens', 'm.bens@yesairways', '0823876349879'),
('Luigi', 'Piagiolo', 'l.piagiolo@yesairways', '0898354932880');


 CREATE TABLE airport (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(20) NOT NULL,
    city VARCHAR(20) NOT NULL,
    country VARCHAR(20) NOT NULL
);





INSERT INTO airport (name, city, country) VALUES
('Tokyo Haneda Airport', 'Tokyo', 'Japan'),
('London Heathrow Airport', 'London', 'United Kingdom'),
('Hong Kong International Airport', 'Hong Kong', 'Hong Kong'),
('Amsterdam Schiphol Airport', 'Amsterdam', 'Netherlands'),
('Frankfurt Airport', 'Frankfurt', 'Germany'),
('Changi Airport', 'Singapore', 'Singapore'),
('Incheon International Airport', 'Seoul', 'South Korea'),
('Johannesburg OR Tambo International Airport', 'Johannesburg', 'South Africa'),
('Sydney Airport', 'Sydney', 'Australia'),
('Kuala Lumpur International Airport', 'Kuala Lumpur', 'Malaysia'),
('Toronto Pearson International Airport', 'Toronto', 'Canada'),
('Chennai International Airport', 'Chennai', 'India'),
('Cairo International Airport', 'Cairo', 'Egypt'),
('JFK Airport', 'New York', 'United States'),
('Lisbon Humberto Delgado Airport', 'Lisbon', 'Portugal');


