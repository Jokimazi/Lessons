# Задание 1 

SELECT games.name AS 'ИГРА', developer_id.name AS 'РАБ', publisher_id.name AS 'Издатель', genres.name AS 'Жанр'
FROM games
JOIN companies AS developer_id ON (games.developer_id = developer_id.id) 
JOIN companies AS publisher_id ON (games.publisher_id = publisher_id.id) 
JOIN genres ON (games.genre_id = genres.id)
LIMIT 100;

# Задание 2

SELECT games.name AS `Название игры`, companies.name AS `Разработчик`, genres.name AS `Жанр`, year_release AS `Год выпуска` FROM games
JOIN companies ON (games.developer_id =companies.id)
JOIN genres ON (games.genre_id = genres.id) 
WHERE games.name LIKE "%NBA 2K20%"; 




# Задание 3 
SELECT games.name AS `Название игры`, genres.name AS `Поджанры игр`
FROM games
JOIN genres ON (games.genre_id = genres.id)
WHERE genres.name = 'ACTION' = genres.id = genres.genre_id;     

# Задание 4
SELECT platforms.name AS "Название платформы", COUNT(games.name) AS "Количество игр"
FROM games
JOIN platforms ON games.platform_id = platforms.id
WHERE games.name LIKE 'Call of Duty%'
GROUP BY platforms.name;     

# Задание 5		
SELECT g1.name AS "Поджанры", g2.name AS "Родительский жанр"
FROM genres g1
JOIN genres g2 ON g1.genre_id = g2.id
WHERE g1.genre_id != 0;

# Задание 6		
SELECT companies.name AS "Издатель", platforms.name AS "Платформа", COUNT(games.name) AS "Количество игр за 2021" from games
JOIN companies ON (games.publisher_id = companies.name)
JOIN platforms ON (games.platform_id = platforms.name)
WHERE games.year_release = 2021 AND platforms.name = "PC"
GROUP BY companies.name, platforms.name;

# Задание 7
SELECT games.name AS "Название игры", COALESCE(regions.name, 'Unknown') AS "Регион"
FROM games
LEFT JOIN regions ON games.region_id = regions.id
LIMIT 50;

# Задание 8
SELECT games.name AS "Название игры", regions.prefix AS "Префикс региона", currencies.prefix AS "Префикс валюты"
FROM games 
LEFT JOIN regions ON games.region_id = regions.id 
LEFT JOIN currencies ON regions.currency_id = currencies.id;