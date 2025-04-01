--Q1-- List the ids of all actors who appeared in “Big Sleep, The”.
SELECT id
FROM actors
WHERE id IN (
    SELECT actorid
    FROM castings
    WHERE movieid = (
        SELECT id
        FROM movies
        WHERE title = "Big Sleep, The"
    )
);

--Q2-- List chronologically the names of the films made by the director of “Citizen Kane”
SELECT title
FROM movies
WHERE director = (
    SELECT director
    FROM movies
    WHERE title = "Citizen Kane")
ORDER BY yr;

--Q3-- List the names of all actors who appeared in “Big Sleep, The”.
SELECT name
FROM actors
WHERE id IN (
    SELECT actorid
    FROM castings
    WHERE movieid = (
        SELECT id
        FROM movies
        WHERE title = "Big Sleep, The"
    )
);

--Q4-- List the ids of all films that were either made in the 1950s or had Elizabeth Taylor in them.
SELECT title
FROM movies
WHERE yr LIKE "195%" OR id IN (
    SELECT movieid
    FROM castings
    WHERE actorid = (
        SELECT id
        FROM actors
        WHERE name = "Elizabeth Taylor"
    )
);

--Q5-- List the name and scores of the film(s) with the best score.
SELECT title, score
FROM movies
WHERE score = (
    SELECT MAX(score)
    FROM movies
);

--Q6-- List the ids the actors with at at least 10 films to their credit.
SELECT id
FROM actors
WHERE id IN (
    SELECT actorid
    FROM castings
    GROUP BY actorid
    HAVING COUNT(actorid) >= 10
);

--Q7-- List the names of the actors with at at least 10 films to their credit.
SELECT name
FROM actors
WHERE id IN (
    SELECT actorid
    FROM castings
    GROUP BY actorid
    HAVING COUNT(actorid) >= 10
);

--Q8-- List the name and scores of the film(s) with scores within 10% of the the best score.
SELECT title, score
FROM movies
WHERE score >= (
    SELECT 0.9 * (MAX(score))
    FROM movies
);

--Q9-- List the names of all the actors that appeared in the most terrible films (those with scores below 3.0).
SELECT DISTINCT(name)
FROM actors
WHERE id IN (
    SELECT actorid
    FROM castings
    WHERE movieid IN (
        SELECT id
        FROM movies
        WHERE score < 3.0
    )
);

--Q10-- List the names and scores of the films with the best and the worst scores.
SELECT title, score
FROM movies
WHERE score = (
    SELECT MAX(score)
    FROM movies
)
OR score = (
    SELECT MIN(score)
    FROM movies
);

--Q11-- List the years and films made before the first film made by the director of ’Citizen Kane’.
SELECT title, yr
FROM movies
where yr < (
    SELECT MIN(yr)
    FROM movies
    WHERE director = (
        SELECT director
        FROM movies
        WHERE title = "Citizen Kane"
    )
)
ORDER BY yr;

--Q12-- List the years and films made after the first film made by the director of ’Citizen Kane’.
SELECT title, yr
FROM movies
where yr > (
    SELECT MIN(yr)
    FROM movies
    WHERE director = (
        SELECT director
        FROM movies
        WHERE title = "Citizen Kane"
    )
)
ORDER BY yr;

--Q13-- List all the films with a score at least as good as the best film made in the 1940s.
SELECT title
FROM movies
WHERE score >= (
    SELECT MAX(score)
    FROM movies
    WHERE yr LIKE "194%"
)

--Q14-- What is the greatest number of films made by any director?
SELECT COUNT(id) as film_count
FROM movies
GROUP BY director
HAVING film_count = (
    SELECT MAX(film_count) 
    FROM (
        SELECT director, COUNT(id) as film_count
        FROM movies 
        GROUP BY director) as subquery);

--Q15-- List the director id and the number of films of the director with the greatest number of films
SELECT director, COUNT(id) as film_count
FROM movies
GROUP BY director
HAVING film_count = (
    SELECT MAX(film_count) 
    FROM (
        SELECT director, COUNT(id) as film_count
        FROM movies 
        GROUP BY director) as subquery);

--Q16-- List, in chronological order, all the films by the director with the greatest number of films.
SELECT title
FROM movies
WHERE director = (    
    SELECT director
    FROM movies
    GROUP BY director
    HAVING COUNT(id) = (
        SELECT MAX(film_count)
        FROM (
            SELECT director, COUNT(id) as film_count
            FROM movies 
            GROUP BY director) as subquery))
ORDER BY yr;

--Q17-- List all the films starring Diane Keaton made by the director of “Bananas”.
SELECT title, id
FROM movies
WHERE director = (
    SELECT director
    FROM movies
    WHERE title = "Bananas"
)
AND id IN (
    SELECT movieid
    FROM castings
    WHERE actorid = (
        SELECT id
        FROM actors
        WHERE name = "Diane Keaton"
    )
);