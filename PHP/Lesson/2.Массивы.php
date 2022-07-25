<?php
$arr = array(11, 22, 33, 44, 55, 66, 33);
// echo($arr), '<br/>';
echo($arr[2]), '<br/>';
echo print_r($arr), '<br/>';
echo var_dump($arr), '<br/>';
echo var_export($arr), '<br/>';

// Различен в выводе данных
$arr2 = ['Имя' => 'Вася', 'Возраст' => 21, 'Класс' => '12A', 'Оценки' => [3, 4, 5, 'Болел'], 'Ученик' => true];
echo var_dump($arr2), '<br/>';
echo $arr2['Класс'], '<br/>';
echo var_export($arr2['Ученик']), '<br/>';
echo $arr2['Ученик'], '<br/>';
echo var_dump($arr2['Ученик']), '<br/>';

$week = [1 => 'pn', 'vt', 'sr', 'ch', 'pt', 'sb']; // Автоиндексация
echo $week[3], '<br/>';
$week[] = 'vs'; // Автодополнение в конец
echo $week[7], '<br/>';
echo count($week), '<br/>';
sort($week); // asort() По убыванию
echo var_export($week), '<br/>';

// Добавляем элемент в именовынный массив
$arr2["Пол"] = "Мальчик";
echo var_export($arr2), '<br/>';

// Проверка наличия в массиве
echo '44 в массиве - ', in_array(44, $arr), '<br/>';
echo '444 в массиве - ', in_array(444, $arr), '<br/>';
echo '"44" в массиве - ', in_array("44", $arr), '<br/>';
echo '"44" в массиве с учетом типа - ', in_array("44", $arr, true), '<br/>';

// Позиция 1 элемента
echo 'Index 33 - ', array_search(33, $arr), '<br/>';
echo 'Все indexЫ 33 - ', print_r(array_keys($arr, 33)), '<br/>';