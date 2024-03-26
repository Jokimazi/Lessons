USE stud_dbd;

SELECT * FROM companies;
SELECT NAME FROM companies;
SELECT NAME AS Имя, region_id AS Регион FROM companies;
SELECT id, NAME, price FROM games LIMIT 3, 10;
SELECT NAME AS Имя, region_id AS Регион FROM companies ORDER BY NAME DESC;
SELECT * FROM games WHERE price = 10;
SELECT * FROM games WHERE year_release = 2020 AND rating < 40;
SELECT * FROM games WHERE price < 30 OR rating > 90;
SELECT * FROM games WHERE price BETWEEN 30 AND 50;
SELECT * FROM games WHERE NAME = "RIDE";
SELECT * FROM games WHERE NAME LIKE "Monster%";
SELECT * FROM games WHERE NAME LIKE "%of%";
SELECT * FROM games WHERE genre_id = 0;

SELECT id, name FROM genres WHERE NAME LIKE "%RPG%";
SELECT * FROM games WHERE genre_id = 20;

SELECT * FROM games WHERE region_id IS not NULL;