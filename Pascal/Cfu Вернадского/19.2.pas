program task;
var w1, w2:string;
i :char;
n : integer;
begin
  
  readln(w1);
  readln(w2);
  for i := 'a' to 'z' do
  begin
  if (pos(i, w1) > 0) and (pos(i, w2) > 0) then
  n := n+1;
  end;
  write(n);
end.