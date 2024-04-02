CREATE TABLE songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    artist TEXT,
    album TEXT,
    genre TEXT,
    duration INTEGER
);

INSERT INTO
    songs (title, artist, album, genre, duration)
VALUES
    ('Song1', 'Artist 1', 'Album 1', 'Pop', 200),
    ('Song2', 'Artist 2', 'Album 2', 'Rock', 300),
    ('Song3', 'Artist 3', 'Album 3', 'Hip Hop', 250),
    ('Song4', 'Artist 4', 'Album 4', 'Electronic', 180),
    ('Song5', 'Artist 5', 'Album 5', 'R&B', 320),
    ('Song6', 'Artist 6', 'Album 6', 'K-pop', 200);

UPDATE songs
SET title = 'New Title'
WHERE id = 1;