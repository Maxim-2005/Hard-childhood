/* Игра жизнь
*   Покидько Максим Сергеевич
*   13.08.2021
*/

var canvas=document.getElementById("canvas"),
    ctx=canvas.getContext("2d"),
    speed=200,
    width,
    height,
    row,
    col,
    size=32;

// Размеры окна
onResize();
window.addEventListener("resize", onResize)
function onResize(){
    width=window.innerWidth;
    height=window.innerHeight;
    canvas.width=width;
    canvas.height=height;
    row=Math.ceil(width/size);
    col=Math.ceil(height/size);
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

// Создаем массив клеток
arr = arrNew();

function arrNew(){
    let arr=[];
    for(let i=0; i<row; i++){
        arr[i]=[];
        for(let j=0; j<col; j++){
            arr[i][j]=true;
        }
    }

    return arr;
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
    for(let i=0; i<row; i++){
        for(let j=0; j<col; j++){
            arr[i][j]=!arr[i][j];
        }
    }
}

function drawCell(){
    ctx.fillStyle="White";
    for(let i=0; i<row; i++){
        for(let j=0; j<col; j++){
            if (arr[i][j]){
                ctx.beginPath();
                ctx.arc(i*size+size/2, j*size+size/2, size/2, 0, 2*Math.PI);
                ctx.fill();
                ctx.closePath()
            }
        }
    }
}
