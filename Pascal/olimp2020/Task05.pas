program Task5;

var
  arr: array[1..20] of integer;
  N, S: integer;

begin
  read(N);
  for var i := 1 to N do
  begin
    read(arr[i]);
    if i < arr[i] then S := S+arr[i];
  end;
  write(S);
end.