program p2;

var N, S, i, x:integer;

begin

writeln('Введите число элементов: ');
readln(N);
S := 0;

for i := 1 to N do
  begin
    read(x);
    if x > i then
      S := S + x;
   end;
  
write('Сумма особых элементов: ', S)

end.

