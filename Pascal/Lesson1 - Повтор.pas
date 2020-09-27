program lesson1;

var
  x: integer;
  StatArr: array[0..5] of integer;
  DynArr: array of integer;

begin
  write('Введите число: ');
  read(x);
  if (x < 10) and (x > 0)
    then writeln('X больше 100')
  else write('X меньше 100');
  while (x > 0) do
  begin
    x := x - 1;
    writeln(x);
  end;
  
  StatArr[0] := 111;
  writeln(StatArr[0]);
  writeln(StatArr);
  
  setlength(DynArr, 10);
  writeln(DynArr);
  
  for var i := 0 to High(DynArr) do
    DynArr[i] := i*i;
  writeln(DynArr);
end.