program Номер31;
var m, n1, n2, n3, n4, t1, t2 :integer;
begin
  read(m);
  
  //Предаем значения переменным
  n1 := (m div 1000);
  n2 := ((m div 100) mod 10);
  n3 := ((m div 10) mod 10);
  n4 := (m mod 10);
  
  //Берем остаток от значения
  n1:=(n1+7) mod 10;
  n2:=(n2+7) mod 10;
  n3:=(n3+7) mod 10;
  n4:=(n4+7) mod 10;
  
  //Меняем 1 и 3 местами
  t1 := n1;
  n1 := n3;
  n3 := t1;
  
  //Меняем 2 и 4 местами1
  t2 := n2;
  n2 := n4;
  n4 := t2;
  
  writeln(n1,n2,n3,n4);
end.