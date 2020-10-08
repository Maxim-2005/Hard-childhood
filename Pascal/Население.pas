//22000 30
Program Task;
var N, I, M, D:int64;
begin
  I := 1;
  M := 0;
  read(N);
  while N > 0 do
   begin
    if N < 0 then
    begin
    N := 0;
    break;
    end;
    I := I*2;
    M := M+1;
    D := I * 4 div 100;
    I := I-D-I*24 div 100;
    N := N-D;
    write(N, ' ');
   end;
 writeln('');
 write(M);
end.