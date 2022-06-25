Просто текст
</br>
<h1>Код HTML</h1>
</br>
<!--Комментарий HTML!-->
<? print("hello world") ?>

<?php
/*
Основы PHP
*/

$x = 2;
echo '<br/>';
echo $x, '<br/>'; // Можно выводить много значений

$x += 2.345; // Преобразует в флоат
echo $x, '<br/>';

print $x; // Выводит одно значение с return 1 (True)
echo '<br/>';

print_r($x); // Форматирует в строку
echo '<br/>';

var_dump($x); // Вывод с типом данных (Для отладки)
echo '<br/>';

var_export($x); // Вывод в формате исполяемоего кода
echo '<br/>';

echo 'Конкотанация $x' . " Склейка строк - $x"; // Одинарные ковычки строка, двойные ковычки строка с переменными
echo '<br/>';

$x = 'Кон'; // Склеивает строки
echo $x .= 'котанация';
echo '<br/>';

$x = null; // Отсутствие данных
var_dump($x); // Единственный способ вывести нулл
echo '<br/>';

echo (int)123.456, '<br/>'; // Отинтовка
echo '<br/>';

// (bull)
// (string)
// (float), (doulbe), (real)
// (array)
// (object)
// (unset) Превращает в нулл
// (binary) бинарный код

// Код HTML(Код PHP(Код HTML(Код JS)))
echo("<script> console.log('from php with love'); </script>");
// Код HTML(Код HTML(Код JS))
?> <script> console.log('from php with love 2'); </script>; <?php
echo '<br/>';

$x = 5;
$y = $x;
echo "x and y = ", $x, ' ', $y, '<br/>';
$x = 111;
echo "x and y = ", $x, ' ', $y, '<br/>';

echo 'Передача поссылки';
echo '<br/>';
$x = 5;
$y = &$x;
echo "x and y = ", $x, ' ', $y, '<br/>';
$x = 111;
echo "x and y = ", $x, ' ', $y, '<br/>';
echo '<br/>';

$zzz = "Колдунство с переменной";
$x = 'zzz'; // Это строка
echo $x, '<br/>';
echo $$x, '<br/>';
echo '<br/>';

$a = 'hello';
$$a = ' world';
echo $a, $$a, '<br/>';
echo "$a ${$a}", '<br/>';
echo "$a $hello";
echo '<br/>';

echo 2 + 2, '<br/>';
echo 2 * 2, '<br/>';
echo 2 / 2, '<br/>';
echo 2 - 2, '<br/>';
echo 100 % 24, '<br/>';
echo abs(-3), '<br/>';
echo min(10, 20, 5), '<br/>';
echo max(10, 20, 5), '<br/>';
echo pow(5, 2), '<br/>';
echo sqrt(16), '<br/>';
echo rand(10, 20), '<br/>';
echo mt_rand(10, 20), '<br/>'; //Более правильный алгоритм
echo 'floor: ', floor(5.9), '<br/>'; //Округление вниз
echo 'ceil: ', ceil(5.1), '<br/>'; //Округление вверх
echo 'round: ', round(4.5), '<br/>'; //Округление
echo 'Число ПИ: ', M_PI, '<br/>'; //Число ПИ
echo 'Число эллера: ', M_E, '<br/>'; //Число эллера
echo '<br/>';

$x = 10;
$y = $x++;
echo 'x++: ', $x, ' ', $y, '<br/>';

$x = 10;
$y = ++$x;
echo '++x: ', $x, ' ', $y, '<br/>';

$x = 10;
$y = $x--;
echo 'x--: ', $x, ' ', $y, '<br/>';

$x = 10;
$y = --$x;
echo '--x: ', $x, ' ', $y, '<br/>';
echo '<br/>';

echo date('d.m.Y H:i'), '<br/>';
echo '<br/>';

echo 2 + '2', '<br/>';
echo '2' + '2', '<br/>';
echo 2 + true, '<br/>';
echo '2' * false, '<br/>';
echo '<br/>';

$x = false;
echo 'empty : ', empty($x), '<br/>';
echo 'isset : ', isset($x), '<br/>';

$x;
echo 'empty : ', empty($x), '<br/>';
echo 'isset : ', isset($x), '<br/>';

$x = 1;
echo 'empty : ', empty($x), '<br/>';
echo 'isset : ', isset($x), '<br/>';

$x = 0;
echo 'empty : ', empty($x), '<br/>';
echo 'isset : ', isset($x), '<br/>';

$x = NULL;
echo 'empty : ', empty($x), '<br/>';
echo 'isset : ', isset($x), '<br/>';

echo strlen('Hello'), '<br/>';
echo trim('      Hello     '), '<br/>';
echo strtoupper('Hello'), '<br/>'; //strtolower
echo 'Хэширование - Hello ', md5('Hello'), '<br/>';
echo 'Хэширование - 0 ', md5('0'), '<br/>';
echo 'Хэширование - Много текста ', md5('qwertyuiopasdfghjklzxcvbnm'), '<br/>';
phpinfo(); 