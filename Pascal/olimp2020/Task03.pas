program Task3;

var
  Y, X, S, A, B, C, D: integer;

begin
  read(A, B, C, D);
  S := A + B + C + D;
  X := S mod 10;
  Y := S div 10 mod 10;
  if (X = 1) and (Y <> 1) then writeln(S, ' птица')
  else
    if ((X = 2) or (X = 3) or (X = 4)) and (Y <> 1) then writeln(S, ' птицы')
  else writeln(S, ' птиц')
end.