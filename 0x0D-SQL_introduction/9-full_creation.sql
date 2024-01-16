-- creates a table called second_table
-- second_table description:
-- id INT
-- name VARCHAR(256)
-- score INT
-- I am not allowed to use the SELECT or SHOW statements
-- the DB name will be passed as argument of mysql command:
-- cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
CREATE TABLE IF NOT EXISTS second_table (
id INT,
name VARCHAR(256),
score INT
);
INSERT INTO second_table (id, name, score) VALUES 
	(1, 'John', 10),
	(2, 'Alex', 3),
	(3, 'Bob', 14),
	(4, 'George', 8)
;
