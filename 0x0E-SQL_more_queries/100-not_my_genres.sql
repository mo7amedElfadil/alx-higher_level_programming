-- uses the hbtn_0d_tvshows database to lists all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use a maximum of two SELECT statement
-- The database name will be passed as an argument of the mysql command
-- cat 100-not_my_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT g.name AS name
FROM tv_genres AS g
LEFT OUTER JOIN
(
SELECT g.name as name, g.id AS g_id
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS sg ON sg.show_id = s.id
LEFT JOIN tv_genres AS g ON sg.genre_id = g.id
WHERE s.title = "Dexter"
) X on g.id = g_id
WHERE X.g_id IS NULL
ORDER BY name
;
