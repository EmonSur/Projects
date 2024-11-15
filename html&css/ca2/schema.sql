DROP TABLE IF EXISTS users;

CREATE TABLE users
(
    user_id TEXT PRIMARY KEY,
    security_q TEXT NOT NULL,
    security_ans TEXT NOT NULL,
    password TEXT NOT NULL
);

DROP TABLE IF EXISTS admins;

CREATE TABLE admins
(
    admin_id TEXT PRIMARY KEY,
    security_q TEXT NOT NULL,
    security_ans TEXT NOT NULL,
    password TEXT NOT NULL
);


DROP TABLE IF EXISTS reviews;

CREATE TABLE reviews
(   
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    review TEXT NOT NULL,
    stars INTEGER NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users (id)
);

DROP TABLE IF EXISTS bookings;

CREATE TABLE bookings
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    adult_tickets INTEGER,
    child_tickets INTEGER,
    booking_date TEXT NOT NULL,
    total_cost INTEGER NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users (id)
);

DROP TABLE IF EXISTS donations;

CREATE TABLE donations
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    donation_amount INTEGER NOT NULL
);



DROP TABLE IF EXISTS animals;

CREATE TABLE animals
(   
    animal_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    species TEXT NOT NULL,
    gender TEXT NOT NULL,
    dob TEXT NOT NULL,
    arrival TEXT NOT NULL,
    habitat TEXT NOT NULL,
    image TEXT
);

INSERT INTO animals (name, species, gender, dob, arrival, habitat, image)
VALUES 
    ('Lyla', 'Lion', 'Female', '2012-07-17', '2014-09-02', 'The African Savanna', 'static/lion.jpg'),
    ('Pepper', 'Giraffe','Female', '2010-07-01', '2014-09-23', 'The African Savanna', 'static/giraffe.jpg'),
    ('Belle', 'Elephant', 'Female', '1989-12-12', '2014-09-25', 'The African Savanna', 'static/elephant.jpg'),
    ('Princess', 'Chimpanzee', 'Female', '1999-09-20', '2014-09-30', 'The African Savanna', 'static/chimpanzee.jpg'),
    ('Trixie', 'Snow Leopard', 'Female', '2003-10-29', '2014-09-04', 'The Himalayian Highlands', 'static/snow_leopard.jpg'),
    ('Spot', 'Red Panda', 'Male', '2008-09-03', '2015-08-11', 'The Himalayan Highlands', 'static/red_panda.jpg'),
    ('Slipper', 'Emperor Penguin', 'Male', '2009-10-2003', '2015-11-12', 'The Freezing Antarctic', 'static/emperor_penguin.jpg'),
    ('Ace', 'Orca', 'Male', '1986-10-22', '2015-01-01', 'The Freezing Antarctic',  'static/orca.jpg'),
    ('Marvin', 'Crocodile', 'Male', '1987-08-31', '2016-11-18', 'The South-American Exhibit', 'static/crocodile.jpg'),
    ('Buttercup', 'Rattlesnake', 'Male', '2014-11-25', '2017-01-18', 'The South-American Exhibit', 'static/rattlesnake.jpg' ),
    ('Cookie', 'Emu', 'Female', '2019-02-08', '2019-02-2-08', 'The Australian Outback', 'static/emu.jpg'),
    ('Rocky', 'Kangaroo', 'Male', '2012-05-09', '2014-09-22', 'The Australian Outback', 'static/kangaroo.jpg');

    

DROP TABLE IF EXISTS employee_info;

CREATE TABLE employee_info
(
    employee_id INTEGER NOT NULL,
    code INTEGER NOT NULL,
    name TEXT NOT NULL,
    dob TEXT NOT NULL,
    job TEXT NOT NULL,
    start_date TEXT NOT NULL
);

INSERT INTO employee_info (employee_id, code, name, dob, job, start_date)
VALUES
    (1, '101', 'Jane O Sullivan', '1988-12-24', 'Caretaker', '2014-06-13');

DROP TABLE IF EXISTS requests_off;

CREATE TABLE requests_off
(
    employee_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    date_begin TEXT NOT NULL,
    date_end TEXT,
    reason TEXT NOT NULL
);

DROP TABLE IF EXISTS requests_off_ans;
