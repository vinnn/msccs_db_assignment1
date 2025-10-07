


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


-- UPDATE flight

UPDATE flight SET {field_to_update} = ? WHERE id= ?




-- SELECT % count of delayed or cancelled flights for year-to-date (YTD) period
SELECT 
CASE 
    WHEN (
        SELECT COUNT(*) FROM flight f 
            WHERE datetime(f.departure_datetime) >= datetime(strftime('%Y-01-01', 'now'))
            AND datetime(f.departure_datetime) < datetime('now')
        ) = 0 
    THEN 0
    ELSE (
        SELECT COUNT(*) FROM flight f 
            WHERE f.status_id={status_id}
            AND datetime(f.departure_datetime) >= datetime(strftime('%Y-01-01', 'now'))
            AND datetime(f.departure_datetime) < datetime('now')
        ) * 100.0 
        / (
        SELECT COUNT(*) FROM flight f 
            WHERE datetime(f.departure_datetime) >= datetime(strftime('%Y-01-01', 'now'))
            AND datetime(f.departure_datetime) < datetime('now')
        )
    END AS result_pc;  



-- SELECT count of future unassigned flights
SELECT COUNT(f.id) AS result_nb
FROM flight f
    JOIN airport a1 ON f.departure_airport_id=a1.id
    JOIN airport a2 ON f.arrival_airport_id=a2.id
    JOIN status s ON f.status_id=s.id
    LEFT JOIN pilot p ON f.pilot_id = p.id
WHERE
    f.pilot_id IS NULL 
    AND datetime(f.departure_datetime) > datetime('now', 'localtime')



    OR p.id IS NULL
ORDER BY f.departure_datetime ASC;  


-- 
-- 
-- PILOT TABLE
-- 
-- 

-- SELECT all pilots
SELECT id, first_name, last_name, email, phone
FROM pilot
ORDER BY id ASC


-- select_all_pilots_available_by_period
SELECT p.id, p.first_name, p.last_name, p.email, p.phone
FROM pilot p
WHERE p.id NOT IN (
    SELECT pilot_id FROM 
    (
        SELECT f.pilot_id AS "pilot_id",
            CASE 
                WHEN strftime('%Y-%m-%d %H:%M', datetime(f.departure_datetime, '+' || f.duration)) < ?
                    OR datetime(f.departure_datetime) > ?
                THEN 0
                ELSE 1
            END AS "clash"
        FROM flight f
        GROUP BY f.pilot_id
        HAVING SUM(clash)>0
    )
    WHERE pilot_id IS NOT NULL
)









-- SELECT total flight time (in “hours:minutes” format) for all pilots for YTD period
SELECT id, first_name, last_name, hours, mins, nb_flights
FROM pilot p
    LEFT JOIN ( 
        SELECT f.pilot_id AS pilot_id, 
            SUM(CAST(strftime('%H', f.duration) AS INTEGER)) +
            SUM(CAST(strftime('%M', f.duration) AS INTEGER)) / 60 AS hours,
            SUM(CAST(strftime('%M', f.duration) AS INTEGER)) % 60 AS mins,
            COUNT(f.id) AS nb_flights
        FROM flight f
        WHERE datetime(f.departure_datetime) >= datetime(strftime('%Y-01-01', 'now'))
            AND datetime(f.departure_datetime) < datetime('now')
        GROUP BY f.pilot_id
    )
    ON p.id=pilot_id
ORDER BY id ASC




-- 
-- 
-- AIRPORT TABLE
-- 
-- 



SELECT id, name, city, country
FROM airport
ORDER BY id ASC





SELECT id, name, city, country
FROM airport
WHERE id
    IN (
        SELECT f.departure_airport_id
        FROM flight f
        WHERE datetime(f.departure_datetime) > datetime('now', 'localtime')
    )
ORDER BY id ASC


SELECT id, name, city, country
FROM airport
WHERE id
    IN (
        SELECT f.arrival_airport_id
        FROM flight f
        WHERE datetime(f.departure_datetime) > datetime('now', 'localtime')
    )
ORDER BY id ASC