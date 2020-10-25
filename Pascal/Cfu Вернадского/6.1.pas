program Task;
var A1, B1, A2, B2, z1, z2, h :integer;
begin
read(A1, B1, A2, B2);
 
if A1 > B1 then z1 := A1
else z1 := B1;

if A2 > B2 then z2 := A2
else z2 := B2;

h := z1+z2;

write(h);
end.