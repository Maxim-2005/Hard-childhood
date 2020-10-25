program task;

var
  x, l, i, j, temp: integer;
  arr: array of integer;

begin
  read(x);
  temp := x;
  while true do
  begin
    x := x div 10;
    if x > 0 then l := l + 1
    else
      break;
  end;
  l := l + 1;
  x := temp;
  setLength(arr, l);
  for i := 0 to l - 1 do
  begin
    arr[i] := x mod 10;
    x := x div 10;
  end;
  for i := 0 to l - 1 do
    for j := i+1 to l - 1 do
    begin
      if arr[i] < arr[j] then
      begin
        temp := arr[i];
        arr[i] := arr[j];
        arr[j] := temp;
      end;
    end;
  x := 0;
  for i := 0 to l - 1 do
    x := x * 10 + arr[i];
  write(x);
end.