-- Import the database dump from hbtn_0d_tvshows_rate to your MySQL server: download (same as 102-rating_shows.sql)

-- Write a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.

-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT g.name, SUM(sr.rate) rating 
FROM tv_genres g 
INNER JOIN tv_show_genres sg 
ON g.id = sg.genre_id 
INNER JOIN tv_show_ratings sr 
ON sg.show_id = sr.show_id 
GROUP BY g.name 
ORDER BY rating DESC;
