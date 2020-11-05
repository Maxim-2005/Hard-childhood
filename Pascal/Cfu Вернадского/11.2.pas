program task;
var N, i, x :integer;
arr: array of integer;
begin
 read(N);
 setLength(arr, N);
 
 for i := 0 to N-1 do
 begin
   read(arr[i]);
 end;
 
 for i := 0 to N-1 do
   if arr[i] = 0 then writeln(2)
    else if arr[i] = 1 then writeln(0)
      else writeln(1);
end.