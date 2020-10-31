program Task;

var
  N, i, S, x: integer;

begin
  S := 0;
  readln(N);
  for i := 1 to N do
  begin
    readln(x);
  if x > 0 then S := S + 1;
  end;
  writeln(S);
end.