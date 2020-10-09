Program Task1;
var V,M,D:integer;
begin
  D := 1;
  M := 1;
  read(V);
  while V > 0 do
  begin
    D :=D+1;
    M :=M*2;
    V :=V-M;
  end;
  write(D);
end.