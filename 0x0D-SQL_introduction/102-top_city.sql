-- displays the top 3 of cities temperature during July and August ordered by temperature (descending) 
-- cat 102-top_city.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month>=7 AND month<=8
GROUP BY city
ORDER BY AVG(value) DESC LIMIT 3;
