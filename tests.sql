


SELECT f.id AS id, 
    date(f.departure_datetime) AS "departure_date", 
    strftime('%H:%M', time(f.departure_datetime)) AS "departure_time",
    strftime('%Y-%m-%d', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_date",
    strftime('%H:%M', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_time",                             
    f.pilot_id AS "pilot_id",
    p.first_name AS "pilot_first_name",
    p.last_name AS "pilot_last_name"             
FROM flight f, pilot p
WHERE f.pilot_id=p.id                         
ORDER BY f.departure_datetime ASC;


-- all flight periods for all pilot
SELECT f.id AS id, 
    date(f.departure_datetime) AS "departure_date", 
    strftime('%H:%M', time(f.departure_datetime)) AS "departure_time",
    strftime('%Y-%m-%d', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_date",
    strftime('%H:%M', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_time",                             
    f.pilot_id AS "pilot_id",
    p.first_name AS "pilot_first_name",
    p.last_name AS "pilot_last_name"             
FROM flight f, pilot p
WHERE f.pilot_id=p.id                         
ORDER BY p.id ASC;



-- individual subqueries to select pilots available during a period (between 2 dates)
-- subquery: flight table with additional column 'clash' = 1 if clash with period else 0  

SELECT f.id AS "id", f.pilot_id AS "pilot_id", 
            f.departure_datetime AS "departure_datetime", 
            strftime('%Y-%m-%d %H:%M', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_datetime",
    CASE 
        WHEN strftime('%Y-%m-%d %H:%M', datetime(f.departure_datetime, '+' || f.duration)) < "2025-10-01 00:00"
            OR f.departure_datetime > "2025-10-06 00:00"
        THEN 0
        ELSE 1
    END AS "clash"
FROM flight f
ORDER BY f.pilot_id ASC;




-- subquery: same then group by pilot_id, with sum(clash) 

SELECT f.id AS "id", f.pilot_id AS "pilot_id", 
            f.departure_datetime AS "departure_datetime", 
            strftime('%Y-%m-%d %H:%M', datetime(f.departure_datetime, '+' || f.duration)) AS "arrival_datetime",
    CASE 
        WHEN strftime('%Y-%m-%d %H:%M', datetime(f.departure_datetime, '+' || f.duration)) < "2025-10-12 06:00"
            OR f.departure_datetime > "2025-10-12 17:00"
        THEN 0
        ELSE 1
    END AS "clash"
FROM flight f
GROUP BY f.pilot_id
HAVING SUM(clash)>0
ORDER BY f.pilot_id ASC;

-- full query: from the pilot table, exclude any pilot which had at least a clash

SELECT p.id, p.first_name, p.last_name
FROM pilot p
WHERE p.id NOT IN (
    SELECT pilot_id FROM 
    (
        SELECT f.pilot_id AS "pilot_id",
            CASE 
                WHEN strftime('%Y-%m-%d %H:%M', datetime(f.departure_datetime, '+' || f.duration)) < "2025-10-12 06:00"
                    OR f.departure_datetime > "2025-10-12 17:00"
                THEN 0
                ELSE 1
            END AS "clash"
        FROM flight f
        GROUP BY f.pilot_id
        HAVING SUM(clash)>0
    )
    WHERE pilot_id IS NOT NULL
);


SELECT * FROM pilot;

DELETE FROM pilot WHERE id=10;


SELECT * FROM flight;