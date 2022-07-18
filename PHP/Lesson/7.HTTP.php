<?php

echo "<h3>Протокол HTTP</h3>";
echo "<h4>GET запросы</h4>";

//http://localhost:3000/7.HTTP.php?x=12345
if (isset($_GET["x"])) {
    echo "Передача значения ", '<br/>';
    $x = $_GET["x"];
    echo "Принято из строки браузера ", $x;
}

//http://localhost:3000/7.HTTP.php?x=Hello&y=World

if (isset($_GET["x"]) && isset($_GET["y"])) {
    echo "Передача нескольких значений ", '<br/>';
    $x = $_GET["x"];
    $y = $_GET["y"];
    echo "Принято из строки браузера ", $x, $y, '<br/><br/>';
}

echo "GET запрос из клика по ссылке", '<br/><br/>';
echo '<a href = "http://localhost:3000/7.HTTP.php?x=Нажата&y=сслыка">Ссылка с вложенным GET запросом</a><br/>';
echo "GET запрос по нажатию кнопки";
?> <form>
    <a href = http://localhost:3000/7.HTTP.php?x=Нажата&y=кнопка>
        <input type = "button" value = "Кнопка с GET запросом">
    </a>
</form><br/><br/> <?php

echo "Пример GET запроса из поля для ввода", '<br/><br/>';
?>
<form method = "GET" action = "http://localhost:3000/7.HTTP.php">
    Введите ваше имя: <input type = "text" name = "y">
    <input type = "submit" name = "x" value = "Привет"/>

</form>
<?php


//Вывод данных
echo "<h5>Данные в массиве_GET</h5>";
var_export($_GET);
echo '<br/><br/>';

echo "<h5>Все данные в GLOBALS</h5>";
var_export($GLOBALS);
echo '<br/><br/>';

