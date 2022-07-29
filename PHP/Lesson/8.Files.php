<?php
namespace Files;

// Подключить файл (Незаменимый файл)
require "5.Функции.php";
// include "x.php"; // Подключение необязательного файла
// Однаразовое подключение
require_once "6.ООП.php";
// include_once "y.php";

// Автозагруза файлов
function autoloader($class){
    echo "Подключение класса $class <br/>";
    include_once $class.'.php';
};
//spl_autoload_register("autoloader");
//$x = new Xclass();

echo "<h3>Импорт пространства имен</h3>";
// $hero = new Hero("Test1", 50); - Неработает
$hero = new \Lessons\Hero("Test1", 50);

use \Lessons\Hero; // Заранее подключить пространство имен
$hero2 = new Hero("Test2", 66);
echo $hero2 -> name, "<br/>";

use \Lessons\Hero as lh; // Тоже самое с псевдонимом
$hero3 = new lh("Test3", 77);
echo $hero3 -> name, "<br/>";

//use \Lessons\{Hero, Unit, SuperHero as Sh};

Use const \Lessons\TEST;
echo TEST, "<br/>";

//use function \Lessons\Имя фунции - Импорт функций

// Файловая система
echo "<h3>Файловая система</h3>";
// die = exit = exit() = exit(0) - Выход из скрипта, возможно с сообщением об ошбике
$file = fopen("Test.txt", "w") or die("Не удалось открыть файл");
//'r+': файл открывается только для чтения с возможностью записи. Если файла не существует, возвращает false
//'w': файл открывается для записи. Если такой файл уже существует, то он перезаписывается, если нет - то он создается
//'w+': файл открывается для записи с возможностью чтения. Если такой файл уже существует, то он перезаписывается, если нет - то он создается
//'a': файл открывается для записи. Если такой файл уже существует, то данные записываются в конец файла, а старые данные остаются. Если файл не существует, то он создается
//'a+': файл открывается для чтения и записи. Если файл уже существует, то данные дозаписываются в конец файла. Если файла нет, то он создается
fwrite($file, "Тестовая запись \r \n"); // Запись файл
fwrite($file, "Еще одна запись".PHP_EOL); // Eще одна Запись файл
fclose($file);