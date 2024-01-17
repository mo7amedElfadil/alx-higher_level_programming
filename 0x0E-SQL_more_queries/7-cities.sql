-- creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)
-- cities description:
--	id INT unique, auto generated, can’t be null and is a primary key
--	state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
--	name VARCHAR(256) can’t be null
-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table cities already exists, your script should not fail
-- cat 7-cities.sql | mysql -hlocalhost -uroot -p
--  echo 'INSERT INTO cities (state_id, name) VALUES (1, "San Francisco");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
-- echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT NOT NULL AUTO_INCREMENT, -- UNIQUE NOT NULL can be ommitted as its a PK
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (state_id) REFERENCES states (id)
	);
