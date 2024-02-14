-- lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_shows.title - rating sum
-- Results must be sorted in descending order by the rating
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
-- cat 102-rating_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows_rate
SELECT
s.title AS title, 
SUM(sr.rate) AS rating
FROM
tv_shows AS s
JOIN tv_show_ratings AS sr ON s.id = sr.show_id
GROUP BY title
ORDER BY rating DESC
;
