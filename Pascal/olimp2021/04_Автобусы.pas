program p4;

var
  N, K, M, S, H: integer;

begin

  readln(N);
  readln(K, M);
  
  S := N div (K + M) * 2;
  H := N - S * ( K + M ) div 2;
  
  if H = 0 then
    S := S
  else if K >= H then
    S := S + 1
  else
    S := S + 2;
  
  writeln(S);

end.