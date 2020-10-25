program Num50;
var s, p, n, n1, n2, n3 :integer;
begin
  n :=0;
  While n<1000 do    
    begin      
      n :=n+1;
      n1 :=n mod 10;
      n2 :=n div 100;
      n3 :=(n mod 100) div 10;
      s :=n1+n2+n3;
      p :=n1*n2*n3;
      if s+50 = p then writeln (n);
    end;
end.