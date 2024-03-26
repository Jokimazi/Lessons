USE stud_dbd;

SELECT COUNT(*) FROM games WHERE year_release = 2020;
SELECT MAX(price), MIN(price) FROM games WHERE price != 0;
SELECT AVG(rating) FROM games WHERE developer_id in
	(SELECT id FROM companies WHERE NAME = 'Valve');
	
SELECT round(AVG(rating), 2) AS 'Средний рейтинг' FROM games WHERE developer_id in
	(SELECT id FROM companies WHERE NAME = 'Valve');
	
SELECT SUM(sales_worldwide) FROM games WHERE year_release = 2021;

SELECT developer_id AS `Разработчик`, 
		 AVG(sales_worldwide) AS `Средние продажи`,
		 year_release
		 FROM games where year_release = 2020 GROUP BY developer_id;

SELECT genre_id, COUNT(*) AS kolvo FROM games GROUP BY genre_id HAVING kolvo > 40;

SELECT developer_id, publisher_id, COUNT(*) FROM games GROUP BY developer_id, publisher_id;

SELECT * FROM games WHERE developer_id = 64 AND publisher_id = 46;

SELECT COUNT(rating) from games WHERE rating > 80 and year_release = 2021;
SELECT COUNT(rating) from games WHERE rating < 40 and year_release = 2021;

SELECT COUNT(genre_id), COUNT(*), COUNT(*) - COUNT(genre_id) FROM genres;
