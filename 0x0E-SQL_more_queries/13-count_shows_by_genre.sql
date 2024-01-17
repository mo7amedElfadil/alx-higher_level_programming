-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre
-- Second column must be called number_of_shows
-- Don’t display a genre that doesn’t have any shows linked
-- Results must be sorted in descending order by the number of shows linked
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
-- tv_show_genres : show_id | genre_id 
-- tv_shows : id | title  
-- tv_genre : id | name 
-- cat 13-count_shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT
	g.name AS genre, 
	COUNT(*) AS number_of_shows
FROM tv_genres g
JOIN tv_show_genres s ON s.genre_id = g.id
GROUP BY g.name
ORDER BY number_of_shows DESC
;
