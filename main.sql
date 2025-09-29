

-- check the table just created:
. schema
-- check the list of tables:
. table



DROP TABLE IF EXISTS flight;
DROP TABLE IF EXISTS schedule;
DROP TABLE IF EXISTS status;
DROP TABLE IF EXISTS pilot;
DROP TABLE IF EXISTS airport;





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




CREATE TABLE flight (
    number VARCHAR(10) PRIMARY KEY,
    originId INTEGER NOT NULL REFERENCES airport(id),
    destinationId INTEGER NOT NULL REFERENCES airport(id),
    departureTime DATE NOT NULL
);

INSERT INTO flight (number, originId, destinationId, departureTime) VALUES
('YESA101', 1, 4, '07:55:00'),
('YESA102', 1, 6, '09:35:00'),
('YESA103', 1, 9, '11:50:00'),
('YESA104', 3, 5, '11:30:00'),
('YESA105', 3, 4, '10:55:00'),
('YESA106', 4, 8, '08:35:00'),
('YESA107', 4, 14, '20:20:00'),
('YESA108', 11, 4, '20:55:00'),
('YESA109', 10, 2, '08:00:00'),
('YESA110', 8, 3, '16:20:00'),
('YESA111', 9, 3, '19:25:00'),
('YESA112', 9, 4, '10:55:00'),
('YESA113', 12, 4, '08:30:00'),
('YESA114', 12, 4, '12:45:00'),
('YESA115', 12, 4, '17:10:00');





CREATE TABLE status (
    id INTEGER PRIMARY KEY,
    description VARCHAR(10) NOT NULL 
);

INSERT INTO status (id, description) VALUES
(0, 'on time'), (1, 'delayed'), (2, 'cancelled');



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


