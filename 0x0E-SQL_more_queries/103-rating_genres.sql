-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
-- cat 103-rating_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows_rate
SELECT
g.name AS name,
SUM(sr.rate) AS rating
FROM
tv_genres AS g
JOIN tv_show_genres AS sg ON sg.genre_id = g.id
JOIN tv_shows AS s ON sg.show_id = s.id
JOIN tv_show_ratings AS sr ON s.id = sr.show_id
GROUP BY name
ORDER BY rating DESC, name
;
