-- lists all cities contained in the database hbtn_0d_usa.
-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
-- cat 9-cities_by_state_join.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
SELECT cities.id, cities.name, states.name
FROM cities
	JOIN states on cities.state_id = states.id
ORDER BY cities.id ASC;
