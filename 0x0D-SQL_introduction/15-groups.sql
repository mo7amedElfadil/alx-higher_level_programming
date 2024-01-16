-- lists the number of records with the same score in the table second_table
-- The result should display:
-- the score
-- the number of records for this score with the label number
-- The list should be sorted by the number of records (descending)
-- cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT score, count(score) AS number
FROM second_table
GROUP BY score
ORDER BY COUNT(score) DESC;
