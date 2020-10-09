Program Task4;
var B,N:integer;
begin
read(B);
while B > 0 do
  begin
   N := N + 1;
   B := B div 10;
  end;
  Write(N);
end.