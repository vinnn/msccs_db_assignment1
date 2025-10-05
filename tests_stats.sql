





-- flight stats
-- YTD number of delayed flights
SELECT COUNT(f.id) 
FROM flight f
WHERE f.status_id=1
    AND datetime(f.departure_datetime) >= datetime(strftime('%Y-01-01', 'now'));


-- % delayed flights this year to date
-- *1.0 is to make sure the nb of flights are accounted as floats for the purpose of the division (avoids integer division)
SELECT 
  CASE 
    WHEN (
        SELECT COUNT(*) FROM flight f 
            WHERE datetime(f.departure_datetime) >= datetime(strftime('%Y-01-01', 'now'))
        ) = 0 
    THEN NULL
    ELSE (
        SELECT COUNT(*) FROM flight f 
            WHERE f.status_id=1
            AND datetime(f.departure_datetime) >= datetime(strftime('%Y-01-01', 'now'))
         ) * 1.0 
        / (
        SELECT COUNT(*) FROM flight f 
            WHERE datetime(f.departure_datetime) >= datetime(strftime('%Y-01-01', 'now'))
        )
    END AS delayed_ytd_pc;




-- YTD number of cancelled flights
SELECT COUNT(f.id) 
FROM flight f
WHERE f.status_id=2
    AND datetime(f.departure_datetime) >= datetime(strftime('%Y-01-01', 'now'));


-- number of scheduled unassigned flights
SELECT COUNT(f.id)
FROM flight f, airport a1, airport a2, status s
LEFT JOIN pilot p ON p.id=f.pilot_id
WHERE
    f.departure_airport_id=a1.id
    AND f.arrival_airport_id=a2.id
    AND f.status_id=s.id
    AND (f.pilot_id IS NULL OR p.id IS NULL)
    AND datetime(f.departure_datetime) > datetime('now', 'localtime')
    ORDER BY f.departure_datetime ASC;







































SELECT strftime('%Y-01-01', 'now')



SELECT COUNT(*) 
FROM flight f
WHERE f.departure_datetime < datetime('now', 'localtime')


SELECT COUNT(*) 
FROM flight f
WHERE datetime(f.departure_datetime) < datetime('now', 'localtime')



SELECT * 
FROM flight f
WHERE f.departure_datetime > datetime('now', 'localtime')

SELECT * 
FROM flight f
WHERE datetime(f.departure_datetime || ':00') > datetime('now', 'localtime')



SELECT * FROM flight
SELECT * FROM pilot


SELECT f.id, f.status_id, f.departure_datetime, f.pilot_id, p.id, p.first_name
FROM flight f
LEFT JOIN pilot p ON p.id=f.pilot_id
WHERE datetime(f.departure_datetime) > datetime('now', 'localtime')

-- datetime(f.a1_datetime || ':00')


SELECT f.id,
    f.status_id,
    f.pilot_id,
    p.id
FROM flight f
LEFT JOIN pilot p ON p.id=f.pilot_id
WHERE
    (f.pilot_id IS NULL OR p.id IS NULL)
    AND f.departure_datetime > datetime('now', 'localtime')
    ORDER BY f.departure_datetime ASC;



SELECT datetime('now');
SELECT datetime('now', 'localtime'); 


SELECT datetime('2025-09-30 11:10');
SELECT '2025-09-30 11:10';


SELECT datetime('2025-06-05 21:50') > datetime('now', 'localtime'); 

