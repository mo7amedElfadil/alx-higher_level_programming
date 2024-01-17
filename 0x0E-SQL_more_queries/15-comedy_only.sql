-- lists all Comedy shows in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
-- cat 15-comedy_only.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT s.title AS title
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS sg ON sg.show_id = s.id
LEFT JOIN tv_genres AS g ON sg.genre_id = g.id
WHERE g.name = "Comedy"
ORDER BY title ASC
;
