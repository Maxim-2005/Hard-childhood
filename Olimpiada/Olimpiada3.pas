Program Olimpiada4;
var a, b, c, d, s:integer;
begin

Writeln('Введите числа 4 видов птиц: ');
Readln(a, b, c, d);
s := a + b + c + d;
Write('Всего ', s, ' птиц');
if ((s mod 10) = 1) and ((s mod 100) <> 11) then Write('а');
if ((s mod 10) > 1) and ((s mod 10) < 5) and (((s mod 100) < 11) or ((s mod 100) > 15)) then Write('ы');
end.