-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use a maximum of two SELECT statement
-- The database name will be passed as an argument of the mysql command
-- cat cat 101-not_a_comedy.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT s.title AS title
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS sg ON s.id = sg.show_id
LEFT JOIN tv_genres AS g ON sg.genre_id = g.id
WHERE s.id NOT IN (
    SELECT DISTINCT s.id
    FROM tv_shows AS s
    JOIN tv_show_genres AS sg ON s.id = sg.show_id
    JOIN tv_genres AS g ON sg.genre_id = g.id
    WHERE g.name = 'Comedy'
)
GROUP BY s.id
ORDER BY title
;
