-- displays the max temperature of each state (ordered by State name).
-- cat 102-top_city.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC
LIMIT 3;
