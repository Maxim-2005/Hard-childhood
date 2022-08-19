--SQLite 3

.help																--Команды трансляторов 
.open Lesson.db												--Создание или открытие базы данных
-- Создание таблицы
CREATE TABLE `user` (
`name` TEXT, 
`age` INTEGER
);

INSERT INTO `user` VALUES('Maxim', 48);	-- Добавляем данные
SELECT * FROM `user`; 									-- Выборка данных
