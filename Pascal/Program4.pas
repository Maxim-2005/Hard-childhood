program P4;

var n, d:integer;

label m;

begin
  
  m:
  
  Write ('Введите число: ');
  Readln (n);
  d := n mod 2;
  
  if d = 0 then Writeln ('Ваше число чётное')
  else Writeln ('Ваше число не чётное');
  
  goto m;
  
end.