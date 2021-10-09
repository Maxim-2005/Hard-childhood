program p1;

var x1, y1, x2, y2, a, b:real;
z : char;

begin
writeln('Введите x1, y1, x2, y2: ');
readln(x1, y1, x2, y2);

a := (y1 - y2) / (x1 - x2);
b := y2 - x2 * a;

if (b >= 0) then
  z := '+'
else
  z := '-';
b := abs(b);

writeln('Уравнение прямой: y = x * ', a, ' + ', b);
end.