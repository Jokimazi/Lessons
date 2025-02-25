USE stud_dbd;

SELECT * FROM games WHERE genre_id = 0;

SELECT id FROM genres WHERE NAME = "Action";

SELECT * FROM games WHERE genre_id = (SELECT id FROM genres WHERE NAME = "Action");

SELECT * FROM games WHERE genre_id = 0 or genre_id = 3;

SELECT * FROM games WHERE genre_id = (SELECT id FROM genres WHERE NAME = "Action");

SELECT id FROM genres WHERE NAME = "Action" OR NAME = "Shooter";

SELECT * FROM games WHERE genre_id in 
	(SELECT id FROM genres WHERE NAME = "Action" OR NAME = "Shooter");

SELECT * FROM games WHERE genre_id IN (0, 3);

SELECT * FROM games WHERE year_release = 2020 and developer_id IN 
	(SELECT id FROM companies WHERE company_id IN 
		(SELECT id FROM companies WHERE NAME like "Xbox%")) AND price > 30;
