
-- check the table just created:
. schema
-- check the list of tables:
. table



DROP TABLE IF EXISTS flight;
DROP TABLE IF EXISTS status;
DROP TABLE IF EXISTS pilot;
DROP TABLE IF EXISTS airport;



-- type of pilot_id, particularly enforced, because this can be null (if a pilot is not assigned)
-- we want to control that this id is either an integer or the NULL value (nothing else):

-- CREATE TABLE flight (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     departure_airport_id INTEGER NOT NULL,
--     arrival_airport_id INTEGER NOT NULL,
--     status_id INTEGER CHECK(status_id IN (0,1,2,3,4)),
--     pilot_id INTEGER CHECK(pilot_id IS NULL OR typeof(pilot_id) = 'integer'),
--     departure_datetime DATETIME,
--     duration TIME NOT NULL,
--     FOREIGN KEY (departure_airport_id) REFERENCES airport(id) ON DELETE RESTRICT,
--     FOREIGN KEY (arrival_airport_id) REFERENCES airport(id) ON DELETE RESTRICT,
--     FOREIGN KEY (status_id) REFERENCES status(id) ON DELETE RESTRICT,
--     FOREIGN KEY (pilot_id) REFERENCES pilot(id) ON DELETE RESTRICT
-- );


CREATE TABLE flight (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    departure_airport_id INTEGER NOT NULL REFERENCES airport(id) ON DELETE RESTRICT,
    arrival_airport_id INTEGER NOT NULL REFERENCES airport(id) ON DELETE RESTRICT,
    status_id INTEGER CHECK(status_id IN (0,1,2,3,4)) REFERENCES status(id) ON DELETE RESTRICT,
    pilot_id INTEGER CHECK(pilot_id IS NULL OR typeof(pilot_id) = 'integer') REFERENCES pilot(id) ON DELETE RESTRICT,
    departure_datetime DATETIME,
    duration TIME NOT NULL
);


-- foreign keys defined as follow will not allow DELETE RESTRICT TO WORK..
-- status_id INTEGER CHECK(status_id IN (0,1,2,3,4)) REFERENCES status(id) ON DELETE RESTRICT
-- => need explicit --- ACTUALLY NOT NEEDED....


-- insert flights in the past in 2024
INSERT INTO flight (departure_airport_id, arrival_airport_id, status_id, pilot_id, departure_datetime, duration) VALUES
(2, 1, 0, 2, '2024-01-30 11:10', '10:00'),
(3, 5, 0, 2, '2024-02-03 08:25', '11:00'),
(5, 4, 1, 2, '2024-02-06 12:20', '06:00'),
(8, 4, 1, 2, '2024-03-20 21:50', '08:00'),
(7, 9, 0, 2, '2024-03-07 12:05', '02:00'),
(7, 4, 0, 5, '2024-08-04 08:35', '10:00'),
(5, 3, 0, 5, '2024-03-12 18:10', '21:00'),
(4, 3, 0, 5, '2024-05-04 16:05', '18:00'),
(3, 7, 1, 5, '2024-07-05 05:35', '19:00'),
(1, 4, 2, 3, '2024-03-28 05:05', '14:00'),
(9, 4, 0, 3, '2024-06-05 21:50', '11:00'), 
(5, 7, 0, 3, '2024-09-05 08:20', '11:00'), 
(8, 2, 0, 3, '2024-09-24 12:05', '12:00'),
(6, 2, 1, 1, '2024-07-05 11:10', '09:00'),
(3, 1, 0, 1, '2024-07-23 16:05', '06:00'),
(3, 4, 0, 1, '2024-08-12 08:30', '08:00'),
(5, 4, 0, 1, '2024-09-08 18:35', '09:00'),
(8, 9, 2, 7, '2024-05-04 09:00', '11:00'),
(8, 4, 2, 7, '2024-06-10 05:20', '11:00'),
(6, 3, 0, 7, '2024-08-12 06:00', '05:00'),
(9, 2, 0, 7, '2024-09-30 07:25', '04:00');

-- insert flights in the past since 1st Jan 2025 until end sep 2025
INSERT INTO flight (departure_airport_id, arrival_airport_id, status_id, pilot_id, departure_datetime, duration) VALUES
(2, 1, 0, 1, '2025-09-30 11:10', '10:00'),
(3, 5, 0, 1, '2025-02-03 08:25', '11:30'),
(5, 4, 1, 1, '2025-02-06 12:20', '06:00'),
(8, 4, 1, 1, '2025-03-20 21:50', '08:50'),
(7, 9, 2, 1, '2025-03-07 12:05', '02:00'),
(7, 4, 0, 1, '2025-08-04 08:35', '10:25'),
(5, 3, 0, 2, '2025-03-12 18:10', '21:00'),
(4, 3, 1, 2, '2025-05-04 16:05', '18:00'),
(3, 7, 0, 2, '2025-07-05 05:35', '19:00'),
(1, 4, 0, 3, '2025-03-28 05:05', '14:00'),
(9, 4, 0, 3, '2025-06-05 21:50', '11:00'), 
(5, 7, 0, 3, '2025-09-05 08:20', '11:00'), 
(8, 2, 2, 3, '2025-09-24 12:05', '12:00'),
(6, 2, 0, 4, '2025-07-05 11:10', '09:00'),
(3, 1, 2, 4, '2025-07-23 16:05', '06:00'),
(3, 4, 0, 4, '2025-08-12 08:30', '08:00'),
(5, 4, 0, 4, '2025-09-08 18:35', '09:00'),
(8, 9, 0, 5, '2025-05-04 09:00', '11:00'),
(8, 4, 0, 5, '2025-06-10 05:20', '11:00'),
(6, 3, 1, 5, '2025-08-12 06:00', '05:00'),
(9, 2, 0, 5, '2025-09-30 07:25', '04:00');

-- insert flights in the future (2026)
INSERT INTO flight (departure_airport_id, arrival_airport_id, status_id, pilot_id, departure_datetime, duration) VALUES
(2, 1, 0, NULL, '2026-01-30 11:10', '10:00'),
(3, 5, 0, 2, '2026-02-03 08:25', '11:00'),
(5, 4, 1, NULL, '2026-02-06 12:20', '06:00'),
(8, 4, 1, NULL, '2026-03-20 21:50', '08:00'),
(7, 9, 0, 2, '2026-03-07 12:05', '02:00'),
(7, 4, 0, 5, '2026-08-04 08:35', '10:00'),
(5, 3, 0, NULL, '2026-03-12 18:10', '21:00'),
(4, 3, 0, NULL, '2026-05-04 16:05', '18:00'),
(3, 7, 1, NULL, '2026-07-05 05:35', '19:00'),
(1, 4, 2, NULL, '2026-03-28 05:05', '14:00'),
(9, 4, 0, NULL, '2026-06-05 21:50', '11:00'), 
(5, 7, 0, NULL, '2026-09-05 08:20', '11:00'), 
(8, 2, 0, NULL, '2026-09-24 12:05', '12:00'),
(6, 2, 1, NULL, '2026-07-05 11:10', '09:00'),
(3, 1, 0, NULL, '2026-07-23 16:05', '06:00'),
(3, 4, 0, 1, '2026-08-12 08:30', '08:00'),
(5, 4, 0, NULL, '2026-09-08 18:35', '09:00'),
(8, 9, 2, 7, '2026-05-04 09:00', '11:00'),
(8, 4, 2, NULL, '2026-06-10 05:20', '11:00'),
(6, 3, 0, NULL, '2026-08-12 06:00', '05:00'),
(9, 2, 0, 7, '2026-09-30 07:25', '04:00');





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
    UNIQUE(first_name, last_name)
);

INSERT INTO pilot (first_name, last_name, email, phone) VALUES
('Steve', 'Lewis', 's.lewis@yesairways.co', '0849384738202'),
('Josh', 'Tambo', 'j.tambo@yesairways.co', '0849389873642'),
('Sylvie', 'Aritin', 's.aritin@yesairways.co', '0839876462737'),
('Joseph', 'Dimst', 'j.dimst@yesairways.co', '0898346493877'),
('Aruna', 'Reno', 'a.reno@yesairways.co', '0837648376438'),
('Bill', 'Farr', 'b.farr@yesairways.co', '0852374203846'),
('Max', 'Himtas', 'm.himtas@yesairways.co', '0899846288872'),
('Bob', 'Hewitt', 'b.hewitt@yesairways.co', '0852837698379'),
('Marina', 'Bens', 'm.bens@yesairways.co', '0823876349879'),
('Luigi', 'Piagiolo', 'l.piagiolo@yesairways.co', '0898354932880');




CREATE TABLE airport (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(40) NOT NULL,
    city VARCHAR(20) NOT NULL,
    country VARCHAR(20) NOT NULL,
    weather VARCHAR(20)
);

INSERT INTO airport (name, city, country, weather) VALUES
('Haneda Airport','Tokyo', 'Japan',''),
('Heathrow Airport','London', 'United Kingdom',''),
('International Airport','Hong Kong', 'Hong Kong',''),
('Schiphol Airport','Amsterdam', 'Netherlands', 'cloudy'),
('Frankfurt Airport','Frankfurt', 'Germany', 'sunny'),
('Changi Airport','Singapore', 'Singapore',''),
('Incheon International Airport','Seoul', 'South Korea',''),
('OR Tambo International Airport','Johannesburg', 'South Africa',''),
('Sydney Airport','Sydney', 'Australia',''),
('International Airport','Kuala Lumpur', 'Malaysia',''),
('Toronto Pearson International Airport','Toronto', 'Canada',''),
('International Airport','Chennai', 'India', 'very hot'),
('International Airport','Cairo', 'Egypt',''),
('JFK Airport','New York', 'United States',''),
('Humberto Delgado Airport','Lisbon', 'Portugal', 'rainy');














