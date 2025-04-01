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
       ('Dumpy Tension of the Divided Unicorn', '2023-02-10'),
       ('Belated Tonic', '2023-02-20'), 
       ('Missing Roller and the Earl', '2023-02-26'),
       ('Glam Blizzard', '2023-03-07'), 
       ('Piscatory Classroom', '2023-03-12'),
       ('Prickly Muse', '2023-03-20'),
       ('Interactive Children of the Phony Filth', '2023-03-29');