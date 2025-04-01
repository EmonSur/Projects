SELECT *
FROM cities
ORDER BY population DESC
--Q1-- List the twenty most populous cities in the world. (MySQL’s LIMIT feature may prove handy here.)
SELECT name
FROM cities
ORDER BY population DESC
LIMIT 20;

--Q2-- List the countries that have at least five cities with a population of one million or more. List the country’s name and the number of such cities.
SELECT cn.name , COUNT(ct.name) AS city_count
FROM countries AS cn
    JOIN cities AS ct ON cn.code = ct.country_code
WHERE ct.population >= 1000000
GROUP BY cn.name
HAVING city_count >= 5;

--Q3-- List all the countries which achieve independence since India did.
SELECT name
FROM countries
WHERE indep_year > (
    SELECT indep_year
    FROM countries
    WHERE name = "India"
);

--Q4-- List those language that are spoken by a significant proportion of the population of at least six countries. (We take 25% or more to be “significant”.)
SELECT cl.language, COUNT(cn.name) AS country_count
FROM countries AS cn 
    JOIN country_languages AS cl ON cn.code = cl.country_code
WHERE cl.percentage >= 25
GROUP BY cl.language
HAVING country_count >= 6;

--Q5-- List the names of all countries that are both among the twenty poorest (lowest GNP
-- per capita) and among the twenty with the lowest life expectancy. Note: take care to
-- filter out countries whose life expectancy, population or GNP is unknown.

--The following two use CTE - something I am unsure we did in class
-- First, for a specific continent
WITH total_area AS (
    SELECT SUM(surface_area) as total_area
    FROM countries
    WHERE continent = "South America"
)
SELECT name, surface_area, total_area, surface_area/total_area as proportion
FROM countries
JOIN total_area ON 1=1
WHERE continent = 'South America' AND surface_area/total_area >= 0.1;

-- Now, for all continents
WITH continents AS (
    SELECT continent, SUM(surface_area) AS total_surface_area
    FROM countries
    GROUP BY continent
)
SELECT c.name, c.continent, c.surface_area, total_surface_area, c.surface_area/total_surface_area AS proportion
FROM countries AS c
JOIN continents ON c.continent = continents.continent
WHERE c.surface_area/total_surface_area >= 0.1;

-- NOT using CTE
-- for a specific continent
SELECT 
    name, 
    surface_area, 
    (SELECT SUM(surface_area) FROM countries WHERE continent = 'South America') as total_area, 
    surface_area/(SELECT SUM(surface_area) FROM countries WHERE continent = 'South America') as proportion
FROM countries
WHERE continent = 'South America' AND surface_area/(SELECT SUM(surface_area) FROM countries WHERE continent = 'South America') >= 0.1;

-- for all continents
SELECT 
    name, 
    continent, 
    surface_area, 
    (SELECT SUM(surface_area) FROM countries WHERE continent = c.continent) as total_area, 
    surface_area/(SELECT SUM(surface_area) FROM countries WHERE continent = c.continent) as proportion
FROM countries c
WHERE surface_area/(SELECT SUM(surface_area) FROM countries WHERE continent = c.continent) >= 0.1;

--Q7-- Calculate what proportion of the world’s total GNP is belongs to the 20 richest (by GNP) countries.
WITH richest_countries AS (
  SELECT gnp
  FROM countries
  WHERE gnp IS NOT NULL AND population IS NOT NULL
  ORDER BY gnp DESC
  LIMIT 20
)
SELECT SUM(richest_countries.gnp) / (SELECT SUM(gnp) FROM countries WHERE gnp > 0.0) as proportion
FROM richest_countries;

--Q8-- Determine the head of state with the greatest amount of territory (by surface area).
SELECT head_of_state
FROM countries
WHERE surface_area = (
    SELECT MAX(surface_area)
    FROM countries
);

--Q9-- List for each continent, the name of the country with the greatest and smallest population.
SELECT continent,
       (SELECT name FROM countries WHERE continent = c1.continent ORDER BY population DESC LIMIT 1) AS largest_pop_country,
       (SELECT name FROM countries WHERE continent = c1.continent ORDER BY population LIMIT 1) AS smallest_pop_country
FROM (SELECT DISTINCT continent FROM countries) AS c1;

--Q10-- For each country in Europe list the percentage of its population that live in its most populous city.
SELECT c.name AS country_name, 
       ci.name AS city_name, 
       ci.population,
       c.population,
       (ci.population/c.population) AS percentage
FROM countries c
JOIN cities ci
  ON c.code = ci.country_code
WHERE c.continent = 'Europe'
  AND ci.population = (SELECT MAX(population) FROM cities WHERE country_code = c.code)

--Q11-- List in descending order of population all countries in which none of the following
-- languages are spoken by a significant proportion of the population: English, Spanish,
-- Chinese, Arabic or Hindi

SELECT name
FROM countries
WHERE name NOT IN (
    SELECT 
)