program prog01;
var x, i:integer;
begin
  read(x);
  for i := 0 to x do
    if i*i > x then
      begin
        x := i*i;
        break;
      end;
    write(x);
end.