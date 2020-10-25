Program P2;

Var A, B, I:Byte;
Rand :word;

Begin
  
randomize;
Rand :=random(1,100);
Writeln (Rand);

case Rand of
1: Write ('Ето раз');
2..50: Write ('Много');
51..100: Write ('Сверх много');
else Write ('Шанс 1/100');
end;

A :=10;
B :=5;
I :=0;

for var G :=0 to 20 do
  Write ('*');
  writeln;
if A>B then 
  begin  
  while I < 8 do
    begin
      Writeln (A+b);
      i := I+1;
    end
  end
else
  repeat 
    Write (A*B);
  until I<4;

End.