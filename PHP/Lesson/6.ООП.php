<?php
namespace Lessons;

use BadFunctionCallException;

define('SIZE', 1920); // Константа
const TEST = "Константа";

class Unit{
    const PI = 3.14;
    public $name;
    private $life;
    protected $pos;

    public function __construct($name, $life = 100){
        $this -> name = $name;
        $this -> life = $life;
        $this -> pos = 200;

    }
    
    public function getLife($pass){
        echo self :: PI, '<br/>';
        if ($pass == "123456")
            return $this -> life;
        else 
            return 0;
    }
}

echo Unit :: PI;
echo '<br/>';
$unit = new Unit('TestName', 50);
echo $unit -> name;
echo '<br/>';
// echo $unit -> life; Ошибка доступа
echo $unit -> getLife('123456');
echo '<br/><br/>';

class Hero extends Unit{
    public static $color = 'black';
    public $armor;

    public function __construct($name, $life){
        parent :: __construct($name, $life); 
        $this -> armor = 1000;
    }

    function __destruct()
    {
        echo "Объект уничтожен";
    }

    public function getPos(){
        echo parent :: PI; // Self - Тоже работает
        echo '<br/>';
        return $this -> pos;
    }

    // Геттеры и Сеттеры
    public function __get($name){
        return $this -> $name;
    }

    public function __set($name, $value){
        $this -> $name = $value;
        return $this -> $name;
    }
}

echo Hero :: $color;
echo '<br/>';
$hero = new Hero('TestName2', 75);
echo $hero -> armor;
echo '<br/>';
// echo $hero -> pos; Ошибка доступа
echo $hero -> getPos();

// Проверка приндалжености объекта к классу
echo "instanceoff hero", $hero instanceof Hero, '<br/>';
echo "instanceoff Unit", $hero instanceof Unit, '<br/>';
echo "instanceoff hero", $unit instanceof Hero, '<br/>';

// Набор функций для вставки в класс
Trait Action {
    public function talk(){
        echo "Я герой", '<br/>';
    }
}

class SuperHero extends Unit {
    use Action;
}

$superHero = new SuperHero('БэтМен', 500);
$superHero -> talk();

// Интерфейс
interface iDrave{
    function update(); // Абстрактный метод
}

// Абстрактный класс (Не имеет объектов для наследования)
abstract class Item{
    function update() {
        echo "Обновление";
    }
}

// $item = new Item(); - Ошибка

// Запечатанный класс (Без наследования)
final class Calc {
    public final function delta(){ // Запечатанная функция
        echo "Запечатанный method";
    }
}