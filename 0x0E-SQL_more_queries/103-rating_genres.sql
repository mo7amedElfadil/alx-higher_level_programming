-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
-- cat 102-rating_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows_rate
SELECT g.name as name, SUM(sr.rate) as rating
FROM tv_genres as g
JOIN tv_show_genres as sg ON sg.genre_id = g.id
JOIN tv_shows as s ON sg.show_id = s.id
JOIN tv_show_ratings as sr ON s.id = sr.show_id
GROUP BY name
ORDER BY rating DESC
;
