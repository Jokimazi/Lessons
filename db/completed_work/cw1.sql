USE stud_db_Klimov;

SELECT * FROM games ORDER BY id DESC LIMIT 15;
SELECT * FROM companies LIMIT 3, 10;
SELECT NAME, sales_worldwide FROM games ORDER BY sales_worldwide DESC LIMIT 20;
SELECT NAME FROM games WHERE year_release = 2016 AND genre_id = 11;
SELECT * FROM games WHERE NAME LIKE "%Final Fantasy%";
SELECT * FROM games WHERE platform_id = 2 AND year_release < 2010;
SELECT * FROM genres WHERE genre_id IS NULL;
SELECT * FROM games WHERE rating > 50 ORDER BY NAME;
SELECT COUNT(*) FROM companies WHERE DESCRIPTION IS NOT NULL;
SELECT * FROM games WHERE year_release <= 2024 AND yestud_dbdar_release >= 1958;