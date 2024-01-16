-- lists all records of the table second_table of the database hbtn_0c_0
-- Don’t list rows without a name value
-- Results should display the score and the name (in this order)
-- Records should be listed by descending score
-- cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
