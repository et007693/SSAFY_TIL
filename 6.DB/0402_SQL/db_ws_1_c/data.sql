SELECT genre, count() as count
FROM songs
GROUP BY genre;

SELECT genre, count() as count, AVG(duration) as average_duration
FROM songs
GROUP BY genre;