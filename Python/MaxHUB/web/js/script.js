/**
Локальный месседжер
Студенты:
- Максим Покидько
18 марта 2024 г.
*/

// Скрипты...
var description=document.getElementById("description");
var download=document.getElementById("download");
var about=document.getElementById("about");
var up=document.getElementById("up");

var footer = document.querySelector("footer");
var footerHeight = footer.offsetHeight;

up.style.visibility = "hidden";

window.addEventListener("load", updateScrollPosition);
window.addEventListener("scroll", updateScrollPosition);

// Загрузка файла
function downloadFile() {
    const file = "file/hub.exe";
    // Создание ссылки на скачивание файла
    const link = document.createElement("a");
    link.href = file;
  
    // Установка атрибута загрузки
    link.setAttribute("download", "");
  
    // Добавление ссылки на страницу и эмуляция клика для скачивания файла
    document.body.appendChild(link);
    link.click();
  
    // Удаление ссылки из DOM после скачивания
    document.body.removeChild(link);
  }

// Плавная прокрутка
document.getElementById('description').addEventListener('click', function() {
    var section1 = document.getElementById('section1');
    var topPos = section1.offsetTop; // Получаем верхнюю позицию раздела 1
    window.scrollTo({
    top: topPos,
    behavior: 'smooth' // Делаем прокрутку плавной
    });
});

document.getElementById('download').addEventListener('click', function() {
    var section2 = document.getElementById('section2');
    var topPos = section2.offsetTop; // Получаем верхнюю позицию раздела 2
    window.scrollTo({
    top: topPos,
    behavior: 'smooth' // Делаем прокрутку плавной
    });
});

document.getElementById('about').addEventListener('click', function() {
    var section3 = document.getElementById('section3');
    var topPos = section3.offsetTop; // Получаем верхнюю позицию раздела 3
    window.scrollTo({
    top: topPos,
    behavior: 'smooth' // Делаем прокрутку плавной
    });
});


// Прыжок на вверх
up.onclick=()=> {
    document.body.scrollTop=0;
    document.documentElement.scrollTop=0;
}

// Что бы кнопка на вверх не залазила на футер
function updateScrollPosition() {
    var windowHeight = window.innerHeight;
    var scrollPosition = window.scrollY;

    if ((scrollPosition + windowHeight) >= (footer.offsetTop - footerHeight)) {
        up.style.bottom = (scrollPosition + windowHeight - footer.offsetTop + footerHeight - 45) + "px";
    } else {
        up.style.bottom = "20px";
    }
}

// Параллакс эффект для фона
document.addEventListener("DOMContentLoaded", function() {
    var header = document.querySelector('header');
    var headerContent = document.querySelector('.header-content');
    var speed = 0.5; // Установите скорость прокрутки (чем меньше значение, тем медленнее)

    window.onscroll = function() {
        var yOffset = window.scrollY;
        header.style.backgroundPositionY = -yOffset * speed + 'px';
        headerContent.style.transform = 'translateY(' + yOffset * speed + 'px)';

        if(document.body.scrollTop>200 || document.documentElement.scrollTop>200)
            up.style.visibility = "visible";
        else
            up.style.visibility = "hidden";
    }
});