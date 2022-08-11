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

<?php
    var_export($GLOBALS);
?>

<?php
    require_once "footer.php";
?>
