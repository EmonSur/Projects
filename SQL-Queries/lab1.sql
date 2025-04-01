--Q1--
SELECT *
FROM students;

--Q2--
SELECT first_name,tt_name
FROM students;

--Q3--
SELECT first_name, _t_name, points
FROM students
ORDER BY points; 

--Q4--
SELECT first_name, last_name, date_of_birth
FROM students
ORDER BY date_of_birth DESC;

--Q5--
SELECT DISTINCT hometown
FROM students;

--Q6--
SELECT first_name, last_name, points
FROM students
WHERE points > 450;

--Q7--
SELECT first_name, last_name, points
FROM students
WHERE points = 525;

--Q8--
SELECT first_name, last_name, points
FROM students 
WHERE points != 525;

--Q9--
SELECT first_name, last_name, points
FROM students
WHERE points > 400 AND points < 500;

--Q10--
SELECT first_name, last_name, hometown
FROM students
WHERE hometown = 'Cork';

--Q11--
SELECT first_name, last_name, date_of_birth
FROM students
WHERE date_of_birth < '1994-01-01';

--Q12--
SELECT first_name, last_name, date_of_birth
FROM students
WHERE date_of_birth > '1992-10-01';

--Q13--
SELECT first_name, last_name, date_of_birth
FROM students
WHERE date_of_birth = '1994-12-25';

--Q14--
SELECT *
FROM students
WHERE first_name = 'Ciara';

--Q15--
SELECT *
FROM students
WHERE first_name = 'ciara';

--Q16--
SELECT *
FROM students
WHERE first_name = 'Barry' OR last_name = 'Barry';

--Q17--
SELECT *
FROM students
WHERE first_name = 'O''Kelly' OR last_name = 'O Kelly';

--Q18--
SELECT first_name, last_name, date_of_birth
FROM students
WHERE date_of_birth > '1994-01-01' AND date_of_birth < '1994-12-31';

--Q19--
SELECT first_name, last_name, hometown
FROM students
WHERE first_name IN ('Aoife', 'Ciara', 'Eimear');

--Q20--
SELECT *
FROM students
WHERE course = 'ck401' OR course = 'ck402';

--Q21--
SELECT *
FROM students
WHERE points > 450 AND hometown = 'Cork';

--Q22--
SELECT *
FROM students
WHERE points > 450 AND hometown != 'Cork';

--Q23--
SELECT *
FROM students
WHERE last_name < (
    SELECT MAX(last_name)
    FROM students 
    WHERE last_name < 'Cuddihy');

--Q24--
SELECT * 
FROM students
WHERE (last_name < 'Callaghan' 
    OR (last_name = 'Callaghan' AND first_name < 'Harry'))
ORDER BY last_name, first_name;

--Q25--
SELECT *
FROM students
WHERE last_name LIKE 'D%';

--Q26--
SELECT first_name as 'Given Name(s)', last_name AS 'Surname', points AS 'CAO Points'
FROM students
WHERE points >= 450
ORDER BY points; 




