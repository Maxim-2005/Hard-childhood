program Task2;

var
  S, A, B, C: integer;

begin
  readln(A, B, C);
  if (A < B) and (A < C) then S := B + C
  else if (C < A) and (C < B) then S := A + B
  else S := A + C;
  write(S);
end.