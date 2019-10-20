Program Paradox;
var priz, void, Bapuant, Bapuant2, G, W :integer;
label m;
begin
  while  G <= 1000 do
  begin
  G :=G+1;
  Writeln ('Игр: ', G, ' Побед: ', W, ' %Побед%: ', W/G*100);
  priz :=random(3)+1;
  writeln('Выберите коробку 1, 2, 3');
  Bapuant :=random (3)+1;
  //Readln(Bapuant);
  writeln('Вы выбрали коробку под номером: ', Bapuant);
  m:
  void :=random(3)+1;
  if (void = Bapuant) or (void = priz) then goto m
  else
  begin
    writeln('В коробке номер: ', void, ' Ничего не оказалось.');
    writeln('Снова сделайте выбор коробки');
    Bapuant2 :=Bapuant;
    While (Bapuant2 = Bapuant) or (Bapuant2 = void) do Bapuant2 :=random (3)+1;
  end;
  if Bapuant2 = priz then
  begin
    writeln('Вы выйграли 1.000.000 рублей!');
    W :=W+1;
  end
    else writeln('Вы проиграли');
  end;
end.