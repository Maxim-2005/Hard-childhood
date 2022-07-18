<?php

function func1 () {
    echo "Привет мир", '<br/><br/>';
}
func1();

function func2 ($x) {
    echo $x, '<br/>';
}
func2('Привет мир');
echo '<br/>';

function func3 ($x) {
    $x *= 2;
    return $x;
    echo 'test'; // Не сработает
}
echo func3(5), '<br/>';

function func4 ($x = 15) {
    $x *= 2;
    return $x;
}
echo func4(10), '<br/>';
echo func4(), '<br/><br/>';

function func5 (string $x) {
    var_dump($x);
}
echo func5(10), '<br/><br/>';

//Анонимные функии
$f = function($x) {
    echo $x;
};
$f("Переменная = анонимная функция <br/><br/>");

$x = fn() => 7 + 8;
echo $x(), '<br/><br/>';