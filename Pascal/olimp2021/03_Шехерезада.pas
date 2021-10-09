program p3;

var N, S: integer;

begin

writeln('Введите число сказок (не меньше 7): ');
readln(N);
S := 0;

while N > 0 do
  begin
    if N mod 3 > 0 then
      begin
        N := N - 5;
        S := S + 1
      end
    else
      begin
        S := S + N div 3;
        break;
      end;
  end;

writeln('Колличество дней: ', S);

end.