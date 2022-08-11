// Casino

// Счетчик кликов
var js_count = 0;

function JS_click() {
    js_count++;
    document.getElementById("js_count").innerHTML = 'JS_COUNT: ' + js_count;
}