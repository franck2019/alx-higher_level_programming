-- Import the database dump from hbtn_0d_tvshows to your MySQL server: 
-- download (same as 16-count_shows_by_genre.sql)

-- script that uses the hbtn_0d_tvshows database to lists all genres not linked to the show Dexter.

-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command

WITH show_genre_dexter AS
(SELECT g.name, g.id
FROM tv_genres g
INNER JOIN tv_show_genres sg
ON g.id = sg.genre_id
INNER JOIN tv_shows s
ON sg.show_id = s.id
WHERE s.title = "Dexter")

SELECT ge.name
FROM tv_genres ge
LEFT JOIN show_genre_dexter sgd
ON ge.id = sgd.id
WHERE sgd.id IS NULL
ORDER BY ge.name;
