Program Task2;
var M,D:integer;
begin
  read(D);
  M := 1;
  while D > 0 do
  begin
    M := M*2;
    D := D-1;
  end;
  Write(M);
end.