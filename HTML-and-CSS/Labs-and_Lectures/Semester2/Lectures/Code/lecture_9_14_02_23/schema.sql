--We must run this file - if we don't do so, an error will appear - no such table

DROP TABLE IF EXISTS gigs;

CREATE TABLE gigs
(
    gig_id INTEGER PRIMARY KEY AUTOINCREMENT,
    band TEXT NOT NULL,
    gig_date TEXT NOT NULL
);

INSERT INTO gigs (band, gig_date)
VALUES ('Decaying Shroom', '2023-01-12'),
       ('Belated Tonic', '2023-01-21'),
       ('Dumpy Tension of Divided Unicorn', '2023-02-10'),
       ('Belated Tonic', '2023-02-20'),
       ('Missing Roler and the Earl', '2023-02-26'),
       ('Glam Blizaard', '2023-03-07'),
       ('Piscatory Classroom', '2023-03-20'),
       ('Prickly Muse', '2023-03-20'),
       ('Interactive Children of the Phony Filth', '2023-03-29');


DROP TABLE IF EXISTS users;

CREATE TABLE users
(
    user_id TEXT PRIMARY KEY,
    password TEXT NOT NULL
);