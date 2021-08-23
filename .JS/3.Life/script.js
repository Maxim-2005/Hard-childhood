/* Игра жизнь
*   Покидько Максим Сергеевич
*   13.08.2021
*/

var canvas=document.getElementById("canvas"),
    ctx=canvas.getContext("2d"),
    btnPlay=document.getElementById("play"),
    btnClear=document.getElementById("clear"),
    btnRnd=document.getElementById("random"),
    speed=100,
    width,
    height,
    row,
    col,
    game=false,
    focus=false,
    size=16;

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

// Старт / Пауза
btnPlay.onclick=()=>{
    focus=true;
    game=!game;
    if (game){
        btnPlay.innerHTML="STOP";
    }
    else
        btnPlay.innerHTML="START";
}

// Рестарт
btnClear.onclick=()=>{
    focus=true;
    arr = arrNew();
    game=false;
}

// Рандомое заполнение
btnRnd.onclick=()=>{
    focus=true;
    arr = arrNew(1);
}

// Мышка
onclick=(e)=>{
    if(!focus){
        let x=Math.floor(e.clientX/size);
        let y=Math.floor(e.clientY/size);
        arr[x][y]=!arr[x][y];
    }
    focus=false;
}

// Цикл анимации
setInterval(() => {
    // Заливка фона
    ctx.fillStyle="orange";
    ctx.fillRect(0, 0, width, height);
    // Сетка
    drawLines();

    //Обновление
    if (game)
        update();

    // Отрисовка точек
    drawCell();

}, speed);

// Создаем массив клеток
arr = arrNew();

function arrNew(param=0){
    let arr=[];
    for(let i=0; i<row; i++){
        arr[i]=[];
        for(let j=0; j<col; j++){
            if(!param)
                arr[i][j]=false;
            else
                arr[i][j]=Math.random()>0.61803;
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
    buffer = copyArr(arr);
    for(let i=1; i<row-1; i++){
        for(let j=1; j<col-1; j++){
            let count=arr[i-1][j-1] + arr[i+1][j+1] + arr[i+1][j-1] + arr[i-1][j+1] + arr[i-1][j] + arr[i+1][j] + arr[i][j-1] + arr[i][j+1];
            if (arr[i][j] == false && (count == 3)){
                buffer[i][j] = true;
            }
            if (arr[i][j] == true && (count < 2 || count > 3)){
                buffer[i][j] = false;
            }
        }
    }
    arr = copyArr(buffer);
}

function copyArr(arr){
    let buffer = [];
    for(let i=0; i<row; i++){
        buffer[i]=[];
        for(let j=0; j<col; j++){
            buffer[i][j]=arr[i][j];
        }
    }
    return buffer;
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
