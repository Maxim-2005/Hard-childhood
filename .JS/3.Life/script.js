/* Игра жизнь
*   Покидько Максим Сергеевич
*   13.08.2021
*/

var canvas=document.getElementById("canvas"),
    ctx=canvas.getContext("2d"),
    speed=200,
    width,
    height,
    x=500,
    size=32;

// Размеры окна
onResize();
window.addEventListener("resize", onResize)
function onResize(){
    width=window.innerWidth;
    height=window.innerHeight;
    canvas.width=width;
    canvas.height=height;
}

function drawLines(){
    ctx.lineWidth=0.25;
    ctx.strokeStyle="chocolate";
    // Горизонтальные линии
    ctx.beginPath();
    for(let i=0; i<height; i+=size){
        ctx.moveTo(0, i);
        ctx.lineTo(width, i);
    }
    ctx.stroke();
    ctx.closePath();

    // Вертикальные линии
    ctx.beginPath();
    for(let i=0; i<width; i+=size){
        ctx.moveTo(i, 0);
        ctx.lineTo(i, height);
    }
    ctx.stroke();
    ctx.closePath();
}

function update(){
    x++;
}

function drawCell(){
    ctx.fillStyle="White";
    ctx.beginPath();
    ctx.arc(x, 500, 16, 0, 2*Math.PI, true);
    ctx.fill();
    ctx.closePath();
}

// Цикл анимации
setInterval(() => {
    // Заливка фона
    ctx.fillStyle="orange";
    ctx.fillRect(0, 0, width, height);
    // Сетка
    drawLines();

    //Обновление
    update();

    // Отрисовка точек
    drawCell();

}, speed);
