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