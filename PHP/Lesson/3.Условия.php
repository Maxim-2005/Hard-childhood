<?php
$x = 5 <=> 6; //Первое меньше -1 первое больше 1 равны 0
echo $x, '<br/>';

if (5 > 3)
    echo '5 > 3', '<br/>';

if (1 === true){
    echo '= по значению и по типу данных', '<br/>';
} else {
    echo 'не = по значению и по типу данных', '<br/>';
}

if (5 > 0 and 5 != 0 || True){
    echo 'Вывод значения', '<br/>';
    echo '<br/>';
} else if (5 < 3 && (1 > 2 or 5 < 3))
    echo "Результат", '<br/>';
else
    echo 'Иначе';
    echo '<br/>';

// Другой синтаксис (Для скриптов)
if (20 > 10):
    echo 20 > 10, '<br/>';
elseif (20 > 0):
    echo 20 > 0, '<br/>';
else:
    echo 'Иначе', '<br/>';
endif;

// Тернарный синтаксис
echo 5 > 2 ? 'Да ' : 'Нет ';
    echo 'Иначе', '<br/>';

$x = 7;
switch ($x){
    case 0:
        echo 'Да x = 0';
    break;
    case 1:
        echo 'Да x = 1';
    break;
    case 5:
        echo 'Да x = 5';
    break;
    default:
        echo 'Все остальное';
    break;
}
echo '<br/>';

match ($x){
    0 => print 'Да match $x = 0',
    1 => print 'Да match $x = 1',
    5 => print 'Да match $x = 5',
    default => print 'Все остальное'
};
echo '<br/>';