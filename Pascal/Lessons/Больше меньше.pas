program P7;

label M;

var a, b, x, y, i : integer;

begin
  
  a := 0;
  b := 1001;
  
  Writeln ('Задумайте число от 1 до 1000');
  M:
  i := i+1;
  x := (a+b) div 2;
  Writeln ('Это число больше(1) или меньше(0) ', x,'?');
  Read (y);
  
  if y = 0 then
    begin
    b := x;
    goto m;
    end;
  if y = 1 then
    begin
    a := x;
    goto m;
    end
  else Writeln ('Ваше число ', x,'. Число попыток: ', i);
  
end.