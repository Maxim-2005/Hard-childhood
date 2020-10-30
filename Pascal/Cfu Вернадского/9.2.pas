program task9;
var
    A, B, C, x1, x2, x3, y1, y2, y3: int64;
begin
    read(A, B);
    y1 := 0;
    y2 := 0;
    y3 := 0;
    while A > 0 do
    begin 
      x1 := A mod 10;
      A := A div 10;
      y1 := y1*10 + x1;
    end;
    
    while B > 0 do
    begin
      x2 := B mod 10;
      B := B div 10;
      y2 := y2*10 + x2;
    end;
    
    C := y1 + y2;
    
    while C > 0 do
    begin
      x3 := C mod 10;
      C := C div 10;
      y3 := y3*10 + x3;
    end;
    write(y3);
end.