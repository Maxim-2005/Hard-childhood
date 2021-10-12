program p5;

var
  m, n, i, S, r, temp: integer;
  q: string;

begin
  temp := 0;
  readln(m, n);
  
  for i := m to n do
  begin
    q := IntToStr(sqr(i));
    r := StrToInt(q.Substring(q.Length - IntToStr(i).Length));

    if i = r then
      begin
      writeln(i);
      temp := 1;
      end;
  end;
    if temp = 0 then
    write(0);
end.