program P9;

uses GraphABC;

const
  M = 100;

var
  r, k: integer;
  arr: array [1..M] of integer;

procedure print;

begin
  
  for var i := 1 to M do Write(' ', arr[i]);
  
end;

begin
  
  for var i := 1 to M do arr[i] := Random(0, 999);
  
  for var i := 1 to M do
    begin
  SetBrushColor(clpink);
  Rectangle (15+i*6, 450, 20+i*6, 450-arr[i] div 3);
  Sleep (arr[i] div 5);
  SetBrushColor(clwhite);
  end;
  
  print;
  Writeln;
  Writeln;
  
  //Сортировка
  
  k := M;
  for var j := 1 to M-1 do  
  begin
    k := k-1;
    for var i := 1 to k do
    begin
      if arr[i] > arr[i + 1] then
      begin
        r := arr[i];
        arr[i] := arr[i + 1];
        arr[i + 1] := r;
        
      end;
    end;
  end;
  
  //clearwindow
  
  print;
  
end.