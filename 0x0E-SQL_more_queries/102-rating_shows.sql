-- lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_shows.title - rating sum
-- Results must be sorted in descending order by the rating
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
-- cat 102-rating_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows_rate
SELECT s.title as title, SUM(sr.rate) as rating
FROM tv_shows as s
JOIN tv_show_ratings as sr ON s.id = sr.show_id
GROUP BY title
ORDER BY RATING DESC
;
