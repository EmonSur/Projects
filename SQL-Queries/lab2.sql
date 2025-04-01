SELECT *
FROM countries;

--Q1-- What is the greatest area of any country?
SELECT name, MAX(area)
FROM countries;

--Q2-- What is the largest population of any country in Africa?
SELECT name, MAX(population)
FROM countries
WHERE region = 'Africa';

--Q3-- What is the total GDP of Europe?
SELECT SUM(gdp)
FROM countries
WHERE region = 'Europe';

--Q4-- List the names an populations of all countries whose GDP is not known (NULL).
SELECT name, population
FROM countries
WHERE gdp IS NULL;

--Q5-- List the names and GDPs of all countries for which a GDP is known.
SELECT name, gdp
FROM countries
WHERE gdp IS NOT NULL;

--Q6-- List the name and average GDP of each region.
SELECT region, AVG(gdp)
FROM countries
GROUP BY region;

--Q7-- List all the countries whose name contains the region name as a substring.
SELECT name
FROM countries
WHERE name LIKE '%' || region || '%';

--Q8-- List the minimum and maximum per capita GDP for each region.
SELECT region, MAX(gdp/population) as 'Max GDP per Capita', MIN(gdp/population) as 'Min GDP per Capita'
FROM countries
GROUP BY region;

-- If we want to exclude countries that have a NULL gdp, we can do the following --
SELECT region, MAX(gdp/population) as 'Max GDP per Capita', MIN(gdp/population) as 'Min GDP per Capita'
FROM countries
WHERE gdp IS NOT NULL
GROUP BY region;
-- SQL already accounts for this though, so there is no need to do this --

--Q9-- List the number of countries and total population for each of the following regions: Europe, Africa and the Middle East.
SELECT region, COUNT(*), SUM(population)
FROM countries
GROUP BY region;

--Q10--  What is the total population, area and GDP of France, Germany and Spain (taken together)?
SELECT SUM(population) as 'Total Population', SUM(area) as 'Total Area', SUM(gdp) as 'Total GDP'
FROM countries
WHERE name IN ('France', 'Germany', 'Spain');

--Q11-- List by region the number of countries in that region with a population greater than 100 million.
SELECT region, COUNT(*)
FROM countries
WHERE population > 100000000
GROUP BY region;

--Q12-- For each letter of the alphabet, list the number countries whose names begin with that letter and the first and last country (alphabetically).
SELECT 
    SUBSTR(name, 1, 1) AS first_letter, 
    COUNT(*) AS 'Country Count', 
    MIN(name) AS 'First Country',
    MAX(name) AS 'Last Country'
FROM countries
GROUP BY first_letter
ORDER BY first_letter;


-- In SQL, the SUBSTR function is used to extract a substring from a given string. The function takes three arguments:

-- 1.The string from which you want to extract a substring.
-- 2.The starting position of the substring within the string.
-- 3.The length of the substring.
-- Like So, SUBSTR('string', starting_position, length);

-- Q13-- List all the countries in the world region by region (alphabetically) and by descending order of population within each region.
SELECT region, name, population
FROM countries
ORDER BY region, population DESC;

--Q14-- List the number of countries and population density (area divided by population) in all regions with total population greater than one billion.
SELECT 
    region, 
    COUNT(*) AS country_count,
    SUM(population)/SUM(area) AS population_density
FROM countries
GROUP BY region
HAVING SUM(population) > 1000000000
ORDER BY population_density;

--Q15-- List the names of all the countries in the same region as Jordan.
SELECT name
FROM countries
WHERE region = (
    SELECT region
    FROM countries
    WHERE name = 'Jordan');

--Q16-- How many countries are in the same region as Jordan?
SELECT region, COUNT(*)
FROM countries
WHERE region = (
    SELECT region
    FROM countries
    WHERE name = 'Jordan')
GROUP BY region;

--Q17-- List those countries in the same region as Spain that have a greater area than Spains’s.
SELECT name
FROM countries
WHERE region = (
    SELECT region
    FROM countries
    WHERE name = 'Spain')
    AND
    area > (
    SELECT area
    FROM countries
    WHERE name = 'Spain');

--Q18-- List all the countries that have an area that is at least 10% of the total area of the region to which they belong.
SELECT name
FROM countries
WHERE area >= (
    SELECT SUM(area) * 0.1
    FROM countries
    WHERE region = countries.region
    GROUP BY region)
    ORDER BY name;

--Q19-- List the countries in decreasing order of population band; for each band list the number of
-- countries and the minimum and maximum area. We use 100 million as our band with, i.e. the
-- first band consists of countries with populations less than 100 million and so on.
SELECT 
    ROUND(population/100000000 + 1) AS band,
    COUNT(*) AS count,
    MIN(area) AS min_area,
    MAX(area) AS max_area
FROM countries
WHERE population IS NOT NULL
GROUP BY band 
ORDER BY band DESC;

--Q20-- What is the minimum population of any country in the same region as China?
SELECT name, MAX(population) AS population
FROM countries
WHERE region = (
    SELECT region
    FROM countries
    WHERE name = 'China')
    AND name != 'China';

--Q21-- 
-- This will will return one row with the name of a random country that has the maximum population, the maximum area, and the maximum GDP. 
-- In other words, it will return the name of a country that is not necessarily the country with the maximum population, area and GDP.

--Q22-- List all the countries whose per capita GDP is at least as great as China’s. The list should appear in descending order order of per capita GDP.
SELECT name, gdp/population AS gdp_per_capita
FROM countries
WHERE gdp_per_capita > (
    SELECT gdp/population AS gdp_per_capita
    FROM countries
    WHERE name = 'China')
ORDER BY gdp_per_capita DESC;