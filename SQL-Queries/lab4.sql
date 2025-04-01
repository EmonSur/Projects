A database called movies has 3 tables. The 1st one is also called movies and contains details about a number of columns, and has the following columns;  id, title, yr (which stands for year), score, votes and director. The 2nd is called actors and contains information about a number of actors and has the following columns; id and name. The last table is called castings and contains which actors are casted in what movies has had the following columns; movieid and actorid. movieid in castings is the same as id in the movies table. actorid in castings is the same as id in actors.

--Q1-- Determine how many films and how many actors are represented in the DB.
SELECT COUNT(DISTINCT m.id) as num_films, COUNT(DISTINCT a.id) as num_actors
FROM movies AS m
JOIN castings AS c ON m.id = c.movieid
JOIN actors a ON c.actorid = a.id;

--Q2-- Determine how many films were released in 1975
SELECT COUNT(DISTINCT id) AS num_films
FROM movies
WHERE yr = 1975;

--Q3-- List the ids of all films in which Clint Eastwood appears.
SELECT DISTINCT c.movieid
FROM castings AS c JOIN actors AS a
WHERE c.actorid = (
    SELECT id
    FROM actors
    WHERE name = 'Clint Eastwood');

--Q4-- List the names and years of all films in which Clint Eastwood appears. Order the filmschronologically.
SELECT DISTINCT title, yr
FROM movies AS m JOIN castings AS c
WHERE m.id IN (
    SELECT DISTINCT c.movieid
    FROM castings AS c JOIN actors AS a
    WHERE c.actorid = (
        SELECT id
        FROM actors
        WHERE name = 'Clint Eastwood'));

--Q5-- List all the actors who appeared in “Citizen Kane”.
SELECT name
FROM actors
WHERE id IN (
    SELECT actorid
    FROM castings
    WHERE movieid = (
        SELECT id
        FROM movies
        WHERE title = 'Citizen Kane'));

--Q6-- List all the actors who appeared in either “Vertigo” or “Rear Window”.
SELECT name
FROM actors
WHERE id IN (
    SELECT actorid
    FROM castings
    WHERE movieid IN (
        SELECT id
        FROM movies
        WHERE title IN ('Rear Window','Veritgo')));

--Q7-- List all the films made by the director with id number 28.
SELECT title
FROM movies
WHERE director = 28;

--Q8-- List all the films made by the director of “Godfather, The”.
SELECT title
FROM movies
WHERE director = (
    SELECT director
    FROM movies
    WHERE title = 'Godfather, The');

--Q9-- List all remakes, i.e. pairs of films with the same name; give the name and the year in each case.
SELECT m1.title, m1.yr, m2.yr
FROM movies m1
JOIN movies m2 ON m1.title = m2.title AND m1.id != m2.id
ORDER BY m1.title;

--Q10-- List the names all obvious sequels with names like “Superman II”( Consider only the first four sequels i.e. II to V).


--Q11-- 

--Q12--

--Q13-- List all the films in which both Clint Eastwood and Richard Burton appeared.
SELECT m.title
FROM movies AS m
    JOIN castings AS c1 ON m.id = c1.movieid
    JOIN castings AS c2 ON m.id = c2.movieid
    JOIN actors AS a1 ON c1.actorid = a1.id
    JOIN actors AS a2 ON c2.actorid = a2.id
WHERE a1.name = 'Clint Eastwood' AND a2.name = 'Richard Burton'
GROUP BY m.title
HAVING COUNT(DISTINCT a1.name) = 1 AND COUNT(DISTINCT a2.name) = 1;

--Q14-- List all the actors who have appeared in a film with Al Pacino.
SELECT name
FROM actors
WHERE id IN (
    SELECT actorid
    FROM castings
    WHERE movieid IN (
        SELECT movieid
        FROM castings
        WHERE actorid = (
            SELECT id
            FROM actors
            WHERE name = 'Al Pacino')));

--Q15-- List all the actors who appeared in both “Big Sleep, The” and “Casablanca”.
SELECT a.name
FROM actors AS a
    JOIN castings AS c1 ON a.id = c1.actorid
    JOIN castings AS c2 ON a.id = c2.actorid
    JOIN movies AS m1 ON c1.movieid = m1.id
    JOIN movies AS m2 ON c2.movieid = m2.id
WHERE m1.title = 'Big Sleep, The' AND m2.title = 'Casablanca'
GROUP BY a.name
HAVING COUNT(DISTINCT m1.title) = 1 AND COUNT(DISTINCT m2.title) = 1;

--Q16-- List all the actors who made a film during the 1950s and also in the 1980s.
SELECT a.name
FROM actors AS a
    JOIN castings AS c1 ON a.id = c1.actorid
    JOIN castings AS c2 ON a.id = c2.actorid
    JOIN movies AS m1 ON c1.movieid = m1.id
    JOIN movies AS m2 ON c2.movieid = m2.id
WHERE m1.yr LIKE "195%" AND m2.yr LIKE "198%"
GROUP BY a.name;

--Q17-- For each year during the 1960s, list the number of films made, and the first and last (alphabetically by title).
SELECT 
    yr AS year, 
    COUNT(*) AS 'Movie Count', 
    MIN(title) AS 'First Movie',
    MAX(title) AS 'Last Movie'
FROM movies
WHERE yr LIKE "196%"
GROUP BY year
ORDER BY year;

--Q18-- List all the actors who appeared in a least ten films and the names of his/her films.
SELECT 
    a.name, 
    COUNT(c.actorid) as film_count,
    GROUP_CONCAT(m.title) as film_names
FROM actors AS a
    JOIN castings AS c ON a.id = c.actorid
    JOIN movies AS m ON c.movieid = m.id
GROUP BY a.name
HAVING film_count >= 10;
