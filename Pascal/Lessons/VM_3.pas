Program Task3;
var M, B,T:integer;
begin
read(M,B);
Writeln(M, ' ',  B);
T := M;
M := B;
B := T;
Writeln(M, ' ',  B);
end.