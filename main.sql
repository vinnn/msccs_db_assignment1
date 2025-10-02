

-- check the table just created:
. schema
-- check the list of tables:
. table



DROP TABLE IF EXISTS flight;
DROP TABLE IF EXISTS status;
DROP TABLE IF EXISTS pilot;
DROP TABLE IF EXISTS airport;
DROP TABLE IF EXISTS location;



CREATE TABLE flight (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    departure_airport_id INTEGER NOT NULL REFERENCES airport(id),
    destination_airport_id INTEGER NOT NULL REFERENCES airport(id),
    status_id INTEGER NOT NULL REFERENCES status(id),
    pilot_id INTEGER REFERENCES pilot(id),
    departure_date DATE NOT NULL,
    departure_time TIME NOT NULL
);

INSERT INTO flight (departure_airport_id, destination_airport_id, status_id, pilot_id, departure_date, departure_time) VALUES
(2, 1, 0, 4, '2025-09-30', '11:05:00'),
(3, 1, 0, 6, '2025-10-03', '08:25:00'),
(5, 4, 1, 9, '2025-10-03', '12:05:00'),
(8, 9, 0, 5, '2025-10-04', '09:00:00'),
(8, 4, 0, 4, '2025-10-10', '05:20:00'),
(6, 3, 0, 8, '2025-10-12', '06:00:00'),
(9, 2, 0, 14, '2025-10-30', '07:25:00');



CREATE TABLE status (
    id INTEGER PRIMARY KEY,
    text VARCHAR(10) NOT NULL 
);

INSERT INTO status (id, text) VALUES
(0, 'on time'), (1, 'delayed'), (2, 'cancelled');




CREATE TABLE pilot (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    email VARCHAR(30) UNIQUE NOT NULL,
    phone VARCHAR(16) UNIQUE NOT NULL,
    current_location_id INTEGER NOT NULL REFERENCES location(id)
);

INSERT INTO pilot (first_name, last_name, email, phone, current_location_id) VALUES
('Steve', 'Lewis', 's.lewis@yesairways', '0849384738202', 4),
('Josh', 'Tambo', 'j.tambo@yesairways', '0849389873642', 6),
('Sylvie', 'Aritin', 's.aritin@yesairways', '0839876462737', 9),
('Joseph', 'Dimst', 'j.dimst@yesairways', '0898346493877', 12),
('Aruna', 'Reno', 'a.reno@yesairways', '0837648376438', 3),
('Bill', 'Farr', 'b.farr@yesairways', '0852374203846', 4),
('Max', 'Himtas', 'm.himtas@yesairways', '0899846288872', 5),
('Bob', 'Hewitt', 'b.hewitt@yesairways', '0852837698379', 2),
('Marina', 'Bens', 'm.bens@yesairways', '0823876349879', 2),
('Luigi', 'Piagiolo', 'l.piagiolo@yesairways', '0898354932880', 4);




CREATE TABLE airport (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(40) NOT NULL,
    location_id INTEGER NOT NULL REFERENCES location(id)
);

INSERT INTO airport (name, location_id) VALUES
('Haneda Airport', 1),
('Heathrow Airport', 2),
('International Airport', 3),
('Schiphol Airport', 4),
('Frankfurt Airport', 5),
('Changi Airport', 6),
('Incheon International Airport', 7),
('OR Tambo International Airport', 8),
('Sydney Airport', 9),
('International Airport', 10),
('Toronto Pearson International Airport', 11),
('International Airport', 12),
('International Airport', 13),
('JFK Airport', 14),
('Humberto Delgado Airport', 15);




CREATE TABLE location (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city VARCHAR(20) NOT NULL,
    country VARCHAR(20) NOT NULL,
    weather VARCHAR(20)
);

INSERT INTO location (city, country, weather) VALUES
('Tokyo', 'Japan',''),
('London', 'United Kingdom',''),
('Hong Kong', 'Hong Kong',''),
('Amsterdam', 'Netherlands', 'cloudy'),
('Frankfurt', 'Germany', 'sunny'),
('Singapore', 'Singapore',''),
('Seoul', 'South Korea',''),
('Johannesburg', 'South Africa',''),
('Sydney', 'Australia',''),
('Kuala Lumpur', 'Malaysia',''),
('Toronto', 'Canada',''),
('Chennai', 'India', 'very hot'),
('Cairo', 'Egypt',''),
('New York', 'United States',''),
('Lisbon', 'Portugal', 'rainy');


