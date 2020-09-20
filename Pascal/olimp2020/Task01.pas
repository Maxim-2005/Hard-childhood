program Task1;
var  N: integer;
begin
  read(N);
  if (N < 100) or (N > 999) then
    writeln('FALSE')
  else
    if ((N div 100) + (N div 10 mod 10) + (N mod 10)) = 13 then
     writeln('ENTER')
    else writeln('LOCK')
end.