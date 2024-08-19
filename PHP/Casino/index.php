<?php // Проект казинои 
    require_once "header.php";
?>

<p>Казино</p>
<!--Счетчик кликов через JS-->
<button type = "button" class = "button" onClick = "JS_click()">
    <output id = "js_count">
        JS_COUNT: 0;
    </output>
</button>

<br/><hr/><br/>

<!--Счетчик кликов через PHP-->
<?php
$count = 0;
if (isset($_POST["php_count"]))
    $count = preg_replace('/[^0-9]/', '', $_POST['php_count']) + 1;
?>
<form method = "post">
    <input type = "submit" name = "php_count" class = "button" value = '<?='PHP-Счетчик: '.$count ?>'>
</form>

<br/><hr/><br/>

<!--Рандом с сервера PHP-->
<?php
    $arr = array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
    $random = '?';
    if (isset($_POST["php_random"]))
        $random = random_int(0, 36);
?>

<form method = "post">
    <input type = "submit" name = "php_random" class = "button" value = '<?='PHP-Рандом: '.$random ?>'>
</form>
<?php 
    $arr[$random] += 1;
    foreach ($arr as $element)
        echo $element, ' ';
?>

<br/><hr/><br/>

<?php
    var_export($GLOBALS);
?>

<?php
    require_once "footer.php";
?>