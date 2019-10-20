Program Olimpiada5;
var 
arr :array[1..20] of integer;
N, s :integer;

begin
  
  Write('Введите число данных от 1 до 20: ');
  Readln(N);
  Writeln('Введите ', N, ' данных');
  for var i := 1 to N do
    begin
       Readln(arr[i]);
       if arr[i] > i then s := s + arr[i];
    end;
  Writeln('Сумма привышающих данных: ', s); 
end.