program P11;

uses GraphABC;

const
  M = 100;

var
  r, k: integer;
  arr: array [1..M] of integer;

procedure print;

begin
  
end;

begin
  //Заполняем массив
  for var i := 1 to M do arr[i] := Random(0, 999);
  
  //Сортировка
  
  k := M;
  for var j := 1 to M - 1 do  
  begin
    k := k - 1;
    for var i := 1 to k do
    begin
      if arr[i] > arr[i + 1] then
      begin
        r := arr[i];
        arr[i] := arr[i + 1];
        arr[i + 1] := r;        
      end;
      lockdrawing;
      clearwindow
    end;
    
    //Отрисовка графика
    for var i := 1 to M do
    begin
      SetBrushColor(clpink);
      Rectangle(15 + i * 6, 450, 20 + i * 6, 450 - arr[i] div 3);
      SetBrushColor(clblack);
    end;
    sleep (100);
    redraw;
  end;
end.