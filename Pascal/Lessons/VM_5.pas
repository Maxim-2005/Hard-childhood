Program Task5;
var M,B,N:integer;
begin
  M:=0;
read(N);
 while N > 0 do
   begin
        B := N mod 10;
        N := N div 10;
        M := M*10 + B;
    end;
Write(M);
end.