-- Import the database dump from hbtn_0d_tvshows to your MySQL server: 
-- download (same as 100-not_my_genres.sql)
-- script that lists allshows without Comedy in the database hbtn_0d_tvshows.

-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
WITH show_title_comedy AS
(SELECT s.title, s.id
FROM tv_shows s
INNER JOIN tv_show_genres sg
ON s.id = sg.show_id
INNER JOIN tv_genres g
ON sg.genre_id = g.id
WHERE g.name = "Comedy")

SELECT sh.title
FROM tv_shows sh
LEFT JOIN show_title_comedy stc
ON sh.id = stc.id
WHERE stc.id IS NULL
ORDER BY sh.title;

