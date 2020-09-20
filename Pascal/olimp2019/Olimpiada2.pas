program Olimpiada2;

var a, b, c, s:integer;

begin
  
  Writeln ('Введите 3 числа');
  Readln (a, b, c);
  
  if (a < b) and (a < c) then s := b + c
  else if (b < a) and (b < c) then s := a + c
  else s := a + b;
  
  Write ('Сумма наибольших значений: ', s);
  
end.