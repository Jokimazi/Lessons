USE stud_dbd;

SELECT NAME, year_release, genre_id FROM games WHERE year_release = 2016 AND genre_id = (SELECT id FROM genres WHERE NAME = "Metroidvania");

SELECT NAME, year_release, platform_id FROM games WHERE year_release < 2010 AND platform_id = (SELECT id FROM platforms WHERE NAME = "PC");

SELECT NAME, price, publisher_id FROM games WHERE price <= 50 AND publisher_id IN (SELECT id FROM companies WHERE NAME = "Nintendo" OR NAME = "Xbox Game Studios");

SELECT AVG(sales_worldwide), year_release FROM games WHERE year_release = 2020;

SELECT MAX(rating), MIN(rating), publisher_id FROM games WHERE publisher_id = (SELECT id FROM companies WHERE NAME = "Square Enix") GROUP BY publisher_id;

SELECT SUM(sales_worldwide) FROM games WHERE NAME LIKE "Halo%";

SELECT COUNT(NAME) FROM games WHERE developer_id = (SELECT id FROM companies WHERE NAME = "Capcom");

SELECT NAME, price, platform_id FROM games WHERE price != 0 AND platform_id = (SELECT id FROM platforms WHERE NAME = "PlayStation 4") ORDER BY price LIMIT 20;

SELECT NAME, year_release, genre_id, platform_id FROM games WHERE 
	year_release = 2021 AND 
	platform_id IN (SELECT id FROM platforms WHERE NAME = "Xbox one") AND
   genre_id IN (SELECT id FROM genres WHERE NAME = "Survival" OR NAME = "Shooter" OR NAME = "Strategy");

SELECT NAME, genre_id FROM games WHERE genre_id IN (SELECT id FROM genres WHERE genre_id = (SELECT id FROM genres WHERE NAME = "Action")) OR genre_id = 0;

