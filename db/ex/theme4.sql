SELECT gm.name, gn.name FROM games AS gm JOIN genres AS gn
		 ON (gm.genre_id = gn.id) order BY gm.name;

SELECT companies.name AS `Разработчик`,
       AVG(games.sales_worldwide) AS `Средние продажи`,
       year_release
       FROM games JOIN companies ON (games.developer_id = companies.id)
       WHERE year_release = 2020 GROUP BY games.developer_id;

SELECT c1.name AS `Разработчик`,
		 c2.name AS `Издатель`,
		 COUNT(*)
		 FROM games JOIN companies AS c1 ON (games.developer_id = c1.id) JOIN companies AS c2
       ON (games.publisher_id = c2.id) GROUP BY c1.name, c2.name ORDER BY c1.name;

SELECT games.name AS `Игра`, 
	    genres.name AS `Жанр`, 
		 regions.name AS `Регион`
		 FROM games JOIN genres ON (games.genre_id = genres.id) 
                  JOIN platforms ON (games.platform_id = platforms.id)
                  LEFT JOIN regions ON (games.region_id = regions.id);
