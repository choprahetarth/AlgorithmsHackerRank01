'''problem lim-> https://www.hackerrank.com/challenges/weather-observation-station-5/problem '''
SELECT CITY,LENGTH(CITY) FROM STATION
ORDER BY LENGTH(CITY) ASC , CITY ASC
LIMIT 1;
SELECT CITY,LENGTH(CITY) FROM STATION
ORDER BY LENGTH(CITY) DESC , CITY DESC
LIMIT 1;