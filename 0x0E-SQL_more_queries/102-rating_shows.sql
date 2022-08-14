-- Import the database hbtn_0d_tvshows_rate dump to your MySQL server: download

-- Write a script that lists all shows from hbtn_0d_tvshows_rate by their rating.

-- Each record should display: tv_shows.title - rating sum
-- Results must be sorted in descending order by the rating
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT s.title, SUM(sr.rate) rating
FROM tv_shows s INNER JOIN tv_show_ratings sr
ON s.id = sr.show_id
GROUP BY s.title
ORDER BY rating DESC;
