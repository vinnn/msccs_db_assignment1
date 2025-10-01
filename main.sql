

-- check the table just created:
. schema
-- check the list of tables:
. table



DROP TABLE IF EXISTS flights;
DROP TABLE IF EXISTS route;
DROP TABLE IF EXISTS status;
DROP TABLE IF EXISTS pilot;
DROP TABLE IF EXISTS airport;





CREATE TABLE flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    routeId VARCHAR(10) NOT NULL REFERENCES route(id),
    statusId INTEGER NOT NULL REFERENCES status(id),
    pilotId INTEGER NOT NULL REFERENCES pilot(id),
    departureDate DATE NOT NULL,
    departureTime TIME NOT NULL
    -- arrivalActualDate DATE NOT NULL, calculated based on duration
    -- arrivalActualTime TIME NOT NULL  calculated based on duration
);

INSERT INTO flights (routeId, statusId, pilotId, departureDate, departureTime) VALUES
(1, 1, 4, '2025-09-30', '11:05:00'),
(3, 1, 6, '2025-10-03', '08:25:00'),
(5, 1, 9, '2025-10-03', '12:05:00'),
(8, 3, 5, '2025-10-04', '09:00:00'),
(8, 3, 4, '2025-10-10', '05:20:00'),
(6, 4, 8, '2025-10-12', '06:00:00'),
(9, 4, 14, '2025-10-30', '07:25:00');




CREATE TABLE route (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    originId INTEGER NOT NULL REFERENCES airport(id),
    destinationId INTEGER NOT NULL REFERENCES airport(id),
    duration TIME NOT NULL
);

INSERT INTO route (originId, destinationId, duration) VALUES
(1, 4, '11:05:00'),
(1, 6, '08:25:00'),
(1, 9, '12:05:00'),
(3, 5, '09:00:00'),
(3, 4, '05:20:00'),
(4, 8, '06:00:00'),
(4, 14, '07:25:00'),
(11, 4, '04:05:00'),
(10, 2, '05:35:00'),
(8, 3, '05:25:00'),
(9, 3, '06:35:00'),
(9, 4, '06:25:00'),
(12, 4, '03:00:00'),
(12, 4, '04:35:00'),
(12, 4, '04:25:00');




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
    country VARCHAR(20) NOT NULL,
    weather VARCHAR(20)
);

INSERT INTO airport (name, city, country, weather) VALUES
('Haneda Airport', 'Tokyo', 'Japan',''),
('Heathrow Airport', 'London', 'United Kingdom',''),
('International Airport', 'Hong Kong', 'Hong Kong',''),
('Schiphol Airport', 'Amsterdam', 'Netherlands', 'cloudy'),
('Frankfurt Airport', 'Frankfurt', 'Germany', 'sunny'),
('Changi Airport', 'Singapore', 'Singapore',''),
('Incheon International Airport', 'Seoul', 'South Korea',''),
('OR Tambo International Airport', 'Johannesburg', 'South Africa',''),
('Sydney Airport', 'Sydney', 'Australia',''),
('International Airport', 'Kuala Lumpur', 'Malaysia',''),
('Toronto Pearson International Airport', 'Toronto', 'Canada',''),
('International Airport', 'Chennai', 'India', 'very hot'),
('International Airport', 'Cairo', 'Egypt',''),
('JFK Airport', 'New York', 'United States',''),
('Humberto Delgado Airport', 'Lisbon', 'Portugal', 'rainy');


