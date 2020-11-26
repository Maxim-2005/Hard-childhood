program task;

var N :integer;

begin
  read(N);
  if N mod 4 = 0 then write(-N)
  else if (N + 1) mod 4 = 0 then write(0)
  else if (N + 2) mod 4 = 0 then write(N+1)
  else write(1);
end.