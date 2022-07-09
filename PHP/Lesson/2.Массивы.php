<?php
$arr = array(11, 22, 33, 44, 55, 66);
//echo($arr), '<br/>';
echo($arr[2]), '<br/>';
echo print_r($arr), '<br/>';
echo var_dump($arr), '<br/>';
echo var_export($arr), '<br/>';

//Различен в выводе данных
$arr2 = ['Имя' => 'Вася', 'Возраст' => 21, 'Класс' => '12A', 'Оценки' => [3, 4, 5, 'Болел'], 'Ученик' => true];
echo var_dump($arr2), '<br/>';
echo $arr2['Класс'], '<br/>';
echo var_export($arr2['Ученик']), '<br/>';
echo $arr2['Ученик'], '<br/>';
echo var_dump($arr2['Ученик']), '<br/>';

$week = [1 => 'pn', 'vt', 'sr', 'ch', 'pt', 'sb']; //Автоиндексация
echo $week[3], '<br/>';
$week[] = 'vs'; // Автодополнение в конец
echo $week[7], '<br/>';
echo count($week), '<br/>';
sort($week); // asort() По убыванию
echo var_export($week), '<br/>';