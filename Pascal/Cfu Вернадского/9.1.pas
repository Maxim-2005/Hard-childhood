program task9;
var N, i, m :integer;
begin
  read(N);
  m := 0;
  
  for i := 1 to trunc(sqrt(N)) do
  begin
    if N mod i = 0 then
      m := m + 1;
  end;
  write(m);
end.