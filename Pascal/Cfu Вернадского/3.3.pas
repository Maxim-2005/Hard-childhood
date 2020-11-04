program taksPi;
var K, i, x : integer;
    V :double;
begin
read(K);
x := 1;

  for i := 0 to K-1 do
  begin
    V := V + 4/(i*2+1)*x;
    x := x*(-1);
  end;
  
  write(V:0:9)
end.