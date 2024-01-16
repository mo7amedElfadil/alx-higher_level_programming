-- creates a table called first_table
-- first_table description:
-- id INT
-- name VARCHAR(256)
-- I am not allowed to use the SELECT or SHOW statements
-- the DB name will be passed as argument of mysql command:
-- cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
CREATE TABLE IF NOT EXISTS first_table (
id INT,
name VARCHAR(256)
);
