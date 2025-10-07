


-- SELECT ALL FUTURE FLIGHTS
-- with explicit INNER JOINs
SELECT f.id AS id, 
    date(f.departure_datetime) AS "departure_date",
    strftime('%H:%M', time(f.departure_datetime)) AS "departure_time",
    strftime('%Y-%m-%d', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_date",
    strftime('%H:%M', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_time",                             
    a1.name AS "departure_airport", a1.city AS "departure_city", a1.country AS "departure_country", 
    a2.name AS "arrival_airport", a2.city AS "arrival_city", a2.country AS "arrival_country", 
    s.text AS "status",
    p.id AS "pilot"
FROM flight f
    JOIN airport a1 ON f.departure_airport_id=a1.id
    JOIN airport a2 ON f.arrival_airport_id=a2.id
    JOIN status s ON f.status_id=s.id
    LEFT JOIN pilot p ON f.pilot_id = p.id
WHERE 
    datetime(f.departure_datetime) > datetime('now', 'localtime')          
ORDER BY datetime(f.departure_datetime) ASC;


-- SELECT all future unassigned flights
-- with explicit INNER JOINs
SELECT f.id AS id,
    date(f.departure_datetime) AS "departure_date",
    strftime('%H:%M', time(f.departure_datetime)) AS "departure_time",
    strftime('%Y-%m-%d', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_date",
    strftime('%H:%M', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_time",              
    a1.name AS "departure_airport", a1.city AS "departure_city", a1.country AS "departure_country",
    a2.name AS "arrival_airport", a2.city AS "arrival_city", a2.country AS "arrival_country", 
    s.text AS "status",
    p.id AS "pilot"
FROM flight f
    JOIN airport a1 ON f.departure_airport_id=a1.id
    JOIN airport a2 ON f.arrival_airport_id=a2.id
    JOIN status s ON f.status_id=s.id
    LEFT JOIN pilot p ON f.pilot_id = p.id
WHERE 
    f.pilot_id IS NULL 
    OR p.id IS NULL
    AND f.departure_datetime > datetime('now', 'localtime')
ORDER BY f.departure_datetime ASC



-- SELECT one flight
-- with explicit INNER JOINs
SELECT f.id AS id, 
    date(f.departure_datetime) AS "departure_date",
    strftime('%H:%M', time(f.departure_datetime)) AS "departure_time",
    strftime('%Y-%m-%d', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_date",
    strftime('%H:%M', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_time",
    f.duration AS "duration",
    a1.name AS "departure_airport", a1.city AS "departure_city", a1.country AS "departure_country",
    a2.name AS "arrival_airport", a2.city AS "arrival_city", a2.country AS "arrival_country",
    s.text AS "status",
    p.id AS "pilot_id", p.first_name AS "pilot_first_name", p.last_name AS "pilot_last_name"
FROM flight f
    JOIN airport a1 ON f.departure_airport_id=a1.id
    JOIN airport a2 ON f.arrival_airport_id=a2.id
    JOIN status s ON f.status_id=s.id
    LEFT JOIN pilot p ON f.pilot_id = p.id
WHERE f.id=?



-- SELECT by departure date
-- with explicit INNER JOINs + remove DISTINCT
SELECT f.id AS id, 
    date(f.departure_datetime) AS "departure_date",
    strftime('%H:%M', time(f.departure_datetime)) AS "departure_time",
    strftime('%Y-%m-%d', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_date",
    strftime('%H:%M', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_time",                             
    a1.name AS "departure_airport", a1.city AS "departure_city", a1.country AS "departure_country", 
    a2.name AS "arrival_airport", a2.city AS "arrival_city", a2.country AS "arrival_country", 
    s.text AS "status",
    p.id AS "pilot"
FROM flight f
    JOIN airport a1 ON f.departure_airport_id=a1.id
    JOIN airport a2 ON f.arrival_airport_id=a2.id
    JOIN status s ON f.status_id=s.id
    LEFT JOIN pilot p ON f.pilot_id = p.id
WHERE 
    strftime('%Y-%m-%d', f.departure_datetime) = strftime('%Y-%m-%d', ?)
ORDER BY f.departure_datetime ASC




-- SELECT by departure airport
-- with explicit INNER JOINs + remove DISTINCT
SELECT f.id AS id, 
    date(f.departure_datetime) AS "departure_date",
    strftime('%H:%M', time(f.departure_datetime)) AS "departure_time",
    strftime('%Y-%m-%d', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_date",
    strftime('%H:%M', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_time",                             
    a1.name AS "departure_airport", a1.city AS "departure_city", a1.country AS "departure_country", 
    a2.name AS "arrival_airport", a2.city AS "arrival_city", a2.country AS "arrival_country", 
    s.text AS "status",
    p.id AS "pilot"
FROM flight f
    JOIN airport a1 ON f.departure_airport_id=a1.id
    JOIN airport a2 ON f.arrival_airport_id=a2.id
    JOIN status s ON f.status_id=s.id
    LEFT JOIN pilot p ON f.pilot_id = p.id
WHERE
    f.departure_airport_id=?
    AND f.departure_datetime > datetime('now', 'localtime')
ORDER BY f.departure_datetime ASC



-- SELECT by arrival airport
-- with explicit INNER JOINs + remove DISTINCT
SELECT f.id AS id, 
    date(f.departure_datetime) AS "departure_date",
    strftime('%H:%M', time(f.departure_datetime)) AS "departure_time",
    strftime('%Y-%m-%d', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_date",
    strftime('%H:%M', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_time",                             
    a1.name AS "departure_airport", a1.city AS "departure_city", a1.country AS "departure_country", 
    a2.name AS "arrival_airport", a2.city AS "arrival_city", a2.country AS "arrival_country", 
    s.text AS "status",
    p.id AS "pilot"
FROM flight f
    JOIN airport a1 ON f.departure_airport_id=a1.id
    JOIN airport a2 ON f.arrival_airport_id=a2.id
    JOIN status s ON f.status_id=s.id
    LEFT JOIN pilot p ON f.pilot_id = p.id
WHERE
    f.arrival_airport_id=?
    AND f.departure_datetime > datetime('now', 'localtime')
    ORDER BY f.departure_datetime ASC


-- SELECT by pilot
-- with explicit INNER JOINs + remove DISTINCT
SELECT f.id AS id, 
    date(f.departure_datetime) AS "departure_date",
    strftime('%H:%M', time(f.departure_datetime)) AS "departure_time",
    strftime('%Y-%m-%d', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_date",
    strftime('%H:%M', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_time",                             
    a1.name AS "departure_airport", a1.city AS "departure_city", a1.country AS "departure_country", 
    a2.name AS "arrival_airport", a2.city AS "arrival_city", a2.country AS "arrival_country", 
    s.text AS "status",
    p.id AS "pilot"
FROM flight f
    JOIN airport a1 ON f.departure_airport_id=a1.id
    JOIN airport a2 ON f.arrival_airport_id=a2.id
    JOIN status s ON f.status_id=s.id
    LEFT JOIN pilot p ON f.pilot_id = p.id
WHERE 
    f.pilot_id=?
    AND datetime(f.departure_datetime) > datetime('now', 'localtime')
ORDER BY f.departure_datetime ASC



-- SELECT past flights
-- with explicit INNER JOINs + remove DISTINCT
SELECT f.id AS id, 
    date(f.departure_datetime) AS "departure_date",
    strftime('%H:%M', time(f.departure_datetime)) AS "departure_time",
    strftime('%Y-%m-%d', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_date",
    strftime('%H:%M', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_time",                             
    a1.name AS "departure_airport", a1.city AS "departure_city", a1.country AS "departure_country", 
    a2.name AS "arrival_airport", a2.city AS "arrival_city", a2.country AS "arrival_country", 
    s.text AS "status",
    p.id AS "pilot"
FROM flight f
    JOIN airport a1 ON f.departure_airport_id=a1.id
    JOIN airport a2 ON f.arrival_airport_id=a2.id
    JOIN status s ON f.status_id=s.id
    LEFT JOIN pilot p ON f.pilot_id = p.id
WHERE 
    f.departure_datetime < datetime('now', 'localtime')                          
    ORDER BY f.departure_datetime DESC



