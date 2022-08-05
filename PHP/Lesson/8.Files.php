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

// use \Lessons\{Hero, Unit, SuperHero as Sh};

Use const \Lessons\TEST;
echo TEST, "<br/>";

// use function \Lessons\Имя фунции - Импорт функций

// Файловая система
echo "<h3>Файловая система</h3>";
// die = exit = exit() = exit(0) - Выход из скрипта, возможно с сообщением об ошбике
$file = fopen("Test.txt", "w") or die("Не удалось открыть файл");
// 'r+': файл открывается только для чтения с возможностью записи. Если файла не существует, возвращает false
// 'w': файл открывается для записи. Если такой файл уже существует, то он перезаписывается, если нет - то он создается
// 'w+': файл открывается для записи с возможностью чтения. Если такой файл уже существует, то он перезаписывается, если нет - то он создается
// 'a': файл открывается для записи. Если такой файл уже существует, то данные записываются в конец файла, а старые данные остаются. Если файл не существует, то он создается
// 'a+': файл открывается для чтения и записи. Если файл уже существует, то данные дозаписываются в конец файла. Если файла нет, то он создается
fwrite($file, "Тестовая запись \r \n"); // Запись файл
fwrite($file, "Еще одна запись".PHP_EOL); // Eще одна Запись файл
fclose($file);

// Чтение файла
$file = fopen("Test.txt", "r") or die("Не удалось открыть файл");
while (!feof($file)){
    $str = htmlentities(fgets($file));
    echo $str, "<br/>";
};
fclose($file);
echo "<br/>";

// Чтение файла полностью
$str = htmlentities(file_get_contents("Test.txt"));
echo "Файл целяком", "<br/>";
echo $str, "<br/>";

// Создание папки
if (mkdir("New folder"))
    echo "Каталог создан", "<br/>";
else
    echo "Ошибка", "<br/>";

// Определение местоположения
$path = getcwd();
echo $path, "<br/>";

// Копирование файла
if (copy("Test.txt", "Test2.txt"))
    echo "Файл скопирован", "<br/>";
else
    echo "Ошибка копирования", "<br/>";

// Перемещение файла
if (rename("Test2.txt", "New Folder/Test3.txt"))
    echo "Файл перемещен", "<br/>";
else
    echo "Ошибка перемещения", "<br/>";

// Удаление файла
if (unlink("New Folder/Test3.txt"))
    echo "Файл удален", "<br/>";
else
    echo "Ошбика", "<br/>";

// Удаление папки
if (rmdir("New folder"))
    echo "Каталог удален", "<br/>";
else
    echo "Ошибка", "<br/>";

// Открытие, чтение и вывод содержимого папок
$dir = getcwd();
if (is_dir($dir)){
    if ($temp = opendir($dir)){ // Открываем каталог
        while (($file = readdir($temp)) !== false){
            echo "Считываем по одному файлу", "<br/>";
            if ($file == '.' || $file == '..') // Пропуск точек
                continue;
            if (is_dir($file))
                echo "Католог $file", "<br/>";
            else
                echo "Файл $file", "<br/>";
        }
        closedir($temp); // Закрываем каталог
    }
}