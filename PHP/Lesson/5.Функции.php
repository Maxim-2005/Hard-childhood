<?php

function func1 () {
    echo "Привет мир", '<br/><br/>';
}
func1();

function func2 ($x) {
    global $z;
    $z = 123;
    echo $x, '<br/>';
}
func2('Привет мир');
echo $z;
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

// Импорт внешних данных
$y = 'Строка';
$f2 = function() use ($y) {
    echo $y, '<br/>';
};

$f2();

// Генератор yield
echo '<br/> <p>Генератор yield</p>';
function func6(){
    yield 1;
    yield 2;
    yield from [3,4];
    yield from new ArrayIterator([5, 6]);
    yield from func7();
    yield 9;
    yield 10;
}

function func7(){
    yield 7;
    yield from func8();
}

function func8(){
    yield 8;
}

//Вызов
foreach(func6() as $x) {
    echo "$x ";
}