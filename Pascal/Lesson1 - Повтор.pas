program lesson1;

var
  x: integer;

begin
  write('Введите число: ');
  read(x);
  if (x < 100) and (x > 0)
    then writeln('X больше 100')
  else write('X меньше 100');
  while (x > 0) do
  begin
    x := x-1;
    writeln(x);
  end;
end.