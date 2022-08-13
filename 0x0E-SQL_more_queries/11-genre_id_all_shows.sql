-- Import the database dump from hbtn_0d_tvshows to your MySQL server:
-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
-- script that lists all shows contained in hbtn_0d_tvshows.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT s.title, sg.genre_id 
FROM tv_shows s 
LEFT JOIN tv_show_genres sg 
ON s.id = sg.show_id
ORDER BY s.title, sg.genre_id;
