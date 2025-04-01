SELECT *
FROM persons

--Q1-- List all the persons in the DB with first names beginning with the letter ’A’
SELECT first_name, last_name
FROM persons
WHERE first_name LIKE 'A%';

--Q2-- List all the persons in the DB with first names that end with the letter ’A’
SELECT first_name, last_name
FROM persons
WHERE first_name LIKE '%A';

--Q3-- List all the persons in the DB whose first names contain the letter ’A’
SELECT first_name, last_name
FROM persons
WHERE first_name LIKE '%A%';

--Q4-- List all the persons in the DB whose first names contains exactly five letters
SELECT first_name
FROM persons
WHERE LENGTH(first_name) = 5;

--Q5-- List all the persons in the DB whose address contains the word “street”
SELECT first_name, last_name
FROM persons
WHERE street LIKE '%street%';

--Q6-- List all the foods that contain a single space
SELECT DISTINCT food
FROM likes
WHERE food LIKE '% %';

--Q7-- List all the foods that contain the pair of letters te
SELECT food
FROM likes
WHERE food LIKE '%te%';



-- Joins Qs --

--Q1-- List the complete cross join of the persons and likes tables.
SELECT *
FROM persons
JOIN likes;

--Q2-- Refine the above so that each row from persons appears adjacent only those rows from
-- likes that relate to the same individual i.e. list each individual together with all his/her
-- favourite foods.
SELECT *
FROM persons JOIN likes 
    ON persons.person_id = likes.person_id;

--Q3-- List Aoife Ahern’s favourite foods.
SELECT *
FROM persons JOIN likes 
    ON persons.person_id = likes.person_id
WHERE persons.first_name = 'Aoife'; 

--Q4-- List the names and favourite foods of all those from County Cork.
SELECT first_name, last_name, food AS favourote_food
FROM persons JOIN likes 
    ON persons.person_id = likes.person_id
WHERE persons.county = 'Cork';

--Q5-- List all the distinct foods favoured by females.
SELECT DISTINCT food
FROM persons JOIN likes 
    ON persons.person_id = likes.person_id
WHERE gender = 'F';

--Q6-- List the names of all individuals who like pizza.
SELECT first_name, last_name
FROM persons JOIN likes 
    ON persons.person_id = likes.person_id
WHERE food = 'Pizza';

--Q7-- List the (distinct) home-towns of those who like beer.
SELECT DISTINCT town
FROM persons JOIN likes 
    ON persons.person_id = likes.person_id
WHERE food = 'Beer';

--Q8-- List the complete cross join of the likes table with itself.

--Q9-- Refine the above so that each row from likes appears adjacent only to other rows from
-- likes that relate to the same individual i.e. list food pairs favoured by some individual.

--Q10-- List the id numbers of those who like both pizza and nutella.
SELECT persons.person_id AS id
FROM persons JOIN likes 
    ON persons.person_id = likes.person_id
WHERE food = 'Nutella' AND food = 'Pizza';

--Q11-- List the id numbers of those who like either pizza or nutella (or both).
SELECT persons.person_id AS id
FROM persons JOIN likes 
    ON persons.person_id = likes.person_id
WHERE food = 'Nutella' OR food = 'Pizza';

--Q12-- List the names of those who live in Cork and who like beer.
SELECT first_name, last_name
FROM persons JOIN likes 
    ON persons.person_id = likes.person_id
WHERE food = 'Beer' AND town = 'Cork';

--Q15-- List the complete cross join of the persons table with itself.

--Q16-- 

--Q17-- List the names of any individuals who share the same date of birth
SELECT first_name, last_name, birth_date, COUNT(*)
FROM persons
GROUP BY birth_date
HAVING COUNT(*) > 1;

--Q18--

--Q19--
SELECT food, COUNT(*)
FROM likes
GROUP BY food
ORDER BY food;

--Q20-- List for each food the number of individuals who count that food among their favourites.
SELECT first_name, last_name
FROM persons
WHERE first_name != (
    SELECT first_name
    FROM persons JOIN likes 
        ON persons.person_id = likes.person_id
    WHERE food = 'Beer');

--Q21-- List those that like at least two of pizza, beer, nutella.
SELECT first_name, last_name, persons.person_id AS id
FROM persons JOIN likes 
    ON persons.person_id = likes.person_id
WHERE food IN ('Beer', 'Pizza', 'Nutella')
GROUP BY id
HAVING COUNT(DISTINCT food) >= 2;

--Q22-- List all distinct pairs of individuals that have at least one food in common.
SELECT DISTINCT p1.first_name, p1.last_name, p2.first_name, p2.last_name
FROM persons AS p1
    JOIN persons AS p2 ON p1.person_id < p2.person_id
    JOIN likes AS f1 ON p1.person_id = f1.person_id
    JOIN likes AS f2 ON p2.person_id = f2.person_id
WHERE f1.food = f2.food;

--Q23-- List for each county and each food the number of individuals in that county that like that food.
SELECT county, food, COUNT(*) as count
FROM persons AS p
    JOIN likes AS f ON p.person_id = f.person_id
GROUP BY county, food
ORDER BY county, food;

--Q24-- List the number of beer lovers county by county in descending order of popularity.
SELECT county, COUNT(*) as beer_lovers
FROM persons AS p
    JOIN likes AS f ON p.person_id = f.person_id
WHERE f.food = 'Beer'
GROUP BY county
ORDER BY beer_lovers DESC;

--Q25-- List the name of the youngest person in the database.
SELECT first_name, last_name, birth_date
FROM persons AS p
WHERE birth_date = (SELECT MAX(birth_date) FROM persons);
