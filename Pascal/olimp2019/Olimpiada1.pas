program Olimpiada1;
var N:word;
begin
write('Введите число от 1 до 10000: ');
read(N);
if (N<100) or (N>999)
then writeln('FALSE')
else
  if N div 100 + (N mod 100) div 10 + N mod 10 = 13
  then writeln('ENTER')
  else writeln('LOCK');
end.