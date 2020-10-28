program task3;

  var n, i, h0, h1, h2, h3 :int64;
    arr: array of int64;

begin
  h1 := 1; h2 := 1; h3 := 1;
  read(n);
  if n < 4 then
    write(1)
  else
    begin
      for i := 4 to n do
      begin
        h0 := h1;
        h1 := h2;
        h2 := h3;
        h3 := h0 + h1 + h2;
      end;
      write(h3);
    end;
end.