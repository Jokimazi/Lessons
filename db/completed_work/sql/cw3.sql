# Задание 1


SElECT COUNT(*) AS 'Общее кол-во компаний', COUNT(DESCRIPTION) AS "Кол-во компаний с описанием", COUNT(*) - COUNT(DESCRIPTION) "Кол-во компаний без описаний" FROM companies;


# Задание 2 
 
SELECT genre_id, COUNT(id) FROM genres WHERE genre_id IS NOT NULL GROUP BY genre_id;


# Задание 3

SELECT genre_id, COUNT(id) FROM genres WHERE genre_id IS NOT NULL AND genre_id != 0 GROUP BY genre_id;

# Задание 4 

SELECT  year_release, COUNT(*) FROM games WHERE year_release <= 2023 GROUP BY year_release ORDER BY year_release DESC;

# Задание 5 


SELECT MAX(rating), COUNT(id) FROM games WHERE year_release = 2020 GROUP BY rating ORDER BY rating DESC  LIMIT 3;

# Задание 6 

SELECT COUNT(*) FROM games WHERE rating > 80 AND platform_id = 

(SELECT id FROM platforms WHERE NAME =  "PC") and genre_id = 

(SELECT id FROM genres WHERE NAME  = "Action");



